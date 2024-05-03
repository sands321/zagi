import sys
sys.path.append('deps')
from fastapi import FastAPI,Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
import uvicorn
import requests
import re

app = FastAPI(openapi_url=None,docs_url=None,redoc_url=None)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    # policy="script-src 'self' http://localhost"
)

@app.get("/")
def hello_world(url:str):
   if not url:
      return {"error":"invalid param"}
   res=requests.get(url)
   res=res.content.decode('utf-8')
   res=re.sub('if\("\[DONE]"===e\.data\)','if(window.zgpt){zgpt.on_msg?.call(this,e)};if("[DONE]"===e.data)',res)
   res=re.sub('if\(null==(\w+)\(\).threads\[n\]\)',r'window.z_gpt=\1;if(null==\1().threads[n])',res)
   r=Response(res)
   return r

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=9000)
