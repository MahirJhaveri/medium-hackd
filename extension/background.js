// background script

chrome.runtime.onMessage.addListener( function (message, sender, sendResponse) {
    if (message.clicked) {
        chrome.tabs.query({'active': true, 'lastFocusedWindow': true}, function (tabs) {
            let url = tabs[0].url;
            url = url.substring(8)
                   chrome.tabs.query({active: true, currentWindow: true}, function(tabs){
                      chrome.tabs.sendMessage(tabs[0].id, {action: {message: "call", url:`https://radiant-brushlands-42789.herokuapp.com/${url}`}}, function(response) {});  
                   })
        });        
    }
  });
  
