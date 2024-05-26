
//eg>>chrome-extension://hienomobjhfbdclmdnihmpppamckjopl/./gpt/assets/index.js
let f_js=`./gpt/assets/index.js`
// let f_js=`http://localhost/zagi/assets/index.js`

function inj_gpt(){
  var script = document.createElement('script');
  script.src = f_js.startsWith(`http`)?f_js:chrome.runtime.getURL(f_js);
  document.head.appendChild(script);
}

inj_gpt()

