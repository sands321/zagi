
async function inj_js_ct(){
  // var scriptContent = `console.log('inj_js_ct>>init')`
  let f_js=`./gpt/assets/index.js`
  //eg>>chrome-extension://hienomobjhfbdclmdnihmpppamckjopl/./gpt/assets/index.js
  let tmp=chrome.runtime.getURL(f_js)
  var scriptContent = await (await fetch(tmp)).text();
  var script = document.createElement('script');
  script.type = 'text/javascript';
  script.textContent = scriptContent;
  (document.head || document.documentElement).appendChild(script);
}
inj_js_ct();
