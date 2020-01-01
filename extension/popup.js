  // popup script
  window.addEventListener('load', (event) => {
    chrome.tabs.executeScript(null, {
      file: 'content.js', //my content script   }, () => {
        // connect() //this is where I call my function to establish a connection     });
    });
  });
  chrome.runtime.sendMessage({clicked : true});