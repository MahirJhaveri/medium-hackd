chrome.extension.onMessage.addListener(function(msg, sender, sendResponse) {
    if (msg.action.message == 'call') {
        window.open(msg.action.url,"_self")
    }
  });