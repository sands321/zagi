
from fastapi import FastAPI
import re,os
from os import path
from jupyter_client import KernelManager
import nbformat
from nbclient import NotebookClient

app = FastAPI(openapi_url=None,docs_url=None,redoc_url=None)

#打印ansi带色字,示例:r'\x1b[32m这是绿色文本\x1b[39m'
def convert_ansi(raw_str):
  ansi_escape_pattern = re.compile(r'\\x1b\[(\d+)(;\d+)*m')
  def replace_with_ansi(match):
      codes = match.group()[3:-1]
      return f'\x1b[{codes}m'
  return ansi_escape_pattern.sub(replace_with_ansi, raw_str)

def execr(cmd):
  return os.popen(cmd).read()

def find_ipy_json():
    lines=execr('ps -ef | grep "ipykernel_launcher -f"')
    lines=[x for x in lines.splitlines() if 'python -m' in x]
    if len(lines)!=1:
      raise Exception(f'err>>find_ipy_json,n_ipy:{lines}')
    line=lines[0]
    f1=re.findall(r'\S+\.json',line)[0]
    return f1

def run_in_ipy(code):
  km=KernelManager()
  f_ipy=f'{path.dirname(__file__)}/../working/zagi.ipynb'
  nb1:NotebookClient=nbformat.read(f_ipy,as_version=4)
  if 1:
    f1=find_ipy_json()
    km.load_connection_file(f1)
    kc=km.client()
    kc.start_channels()
  nb_cl1=NotebookClient(nb=nb1,km=km,kernel_name='python3')
  nb_cl1.kc=kc
  #---
  ls_cell=nb1['cells']
  nb_nd1=nbformat.v4.new_code_cell(code)
  if len(ls_cell)==1 and ls_cell[0].source=='':
    del ls_cell[0]
  nb1['cells'].append(nb_nd1)
  #debug
  nbformat.write(nb1,f_ipy)
  try:
    nb_cl1.execute_cell(nb_nd1,len(ls_cell)-1,execution_count=1)
  except Exception as e:
    print(e)
  nb_nd1['outputs'][0]['execution_count']=1
  nbformat.write(nb1,f_ipy)
  rst_b=nb_nd1['outputs'][-1]
  #error,stream(name=stdout,text),execute_result({data:text/plain})
  #1.!pip@仅stream
  rst_t=rst_b['output_type']
  is_err=rst_t=='error'
  #报错
  if is_err:
    #ename,evalue,traceback
    rst=rst_b['traceback'][0]
  elif rst_t=='execute_result':
    rst=rst_b['data']['text/plain']
  elif rst_t=='stream':
    rst=rst_b['text']
  kc.stop_channels()
  return int(is_err),rst,'python:cheng'

@app.get("/zagi/code")
def wgpt_code(v:str):
  print(f'a=======\n{v}\nb=======')
  err,rst,_=run_in_ipy(v)
  print(f'code>>err:{err},rst:',convert_ansi(rst),sep='\n')
  #空输出gpts会卡住
  if not err and (rst is None or rst.strip('')==''):
    rst='success'
  return {"is_error":err,"output":rst}