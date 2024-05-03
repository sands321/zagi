chrome.webRequest.onBeforeRequest.addListener(
  function (details) {
    let url = details?.url;
    if(url.match('cdn.oaistatic.com/_next/static/chunks/pages/_app-.+') || url.match('cdn.oaistatic.com/_next/static/chunks/3445-.+')){
      console.log(`onBeforeReq>>${url}`);
      let newUrl=`https://service-qou1kosp-1253869226.bj.tencentapigw.com.cn/release/?url=${url}`
      // let newUrl=`http://localhost/zagi/api/mock?url=${url}`
      return {redirectUrl:newUrl};
    }
    return {};
  },
  // { urls: ['<all_urls>'] },
  //GPT=>
  //https://cdn.oaistatic.com/_next/static/chunks/pages/_app-93968d3a427959c6.js?dpl=22e6a30614e462a1a0f4f5c312690d8f16d620cb
  //https://cdn.oaistatic.com/_next/static/chunks/3445-6f29d2304bed4863.js?dpl=42860926fb84fd5013b1a02926423c7c761b2e06
  { urls: ['https://cdn.oaistatic.com/_next/static/chunks/pages/_app-*.js*', 'https://cdn.oaistatic.com/_next/static/chunks/3445-*.js*'] },
  ["blocking"]
);

chrome.webRequest.onHeadersReceived.addListener(
  function(details) {
    let url=details.url;
    let lsHd=details.responseHeaders
    let n_old=lsHd.length;
    //可能多个csp
    for (let i = lsHd.length-1; i >=0 ; i--) {
      if (lsHd[i].name.toLowerCase() === 'content-security-policy') {
        lsHd.splice(i, 1);
      }
    }
    console.log(`onHeadersReceived>>n_del:${n_old-lsHd.length},n_hd:${n_old}->${lsHd.length},url:${url}`);
    // console.log(`resHeaders>>\n${JSON.stringify(lsHd)}`);
    return {responseHeaders: lsHd};
  },
  {urls: [
    "https://chat.openai.com/*",
  ]},
  ["blocking", "responseHeaders"]
);




