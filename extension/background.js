// background script
chrome.runtime.onMessage.addListener( function (message, sender, sendResponse) {
    if (message.clicked) {
        chrome.tabs.query({'active': true, 'lastFocusedWindow': true}, function (tabs) {
            let url = tabs[0].url;
            console.log(url)
            
        });        
    }
  });
  
