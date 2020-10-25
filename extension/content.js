chrome.extension.onMessage.addListener(function (msg, sender, sendResponse) {
    console.log("sa")
    if (msg.action.message == 'call') {
        window.open(msg.action.url, "_self")
    }
});
chrome.storage.local.get("check", function (result) {
    console.log(result.check)
    if (result.check) {
        var link = document.createElement("link");
        link.href = "https://japsuchiha.me/medium.css";
        link.type = "text/css";
        link.rel = "stylesheet";
        document.getElementsByTagName("head")[0].appendChild(link);
    }
});

// var link = document.createElement("link");
// link.href = "https://japsuchiha.me/medium.css";
// link.type = "text/css";
// link.rel = "stylesheet";
// document.getElementsByTagName("head")[0].appendChild(link);