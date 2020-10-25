  // popup script

  let btn = document.querySelector(".btn")
  console.log(btn)
  let check = document.querySelector(".check")
  console.log(check)

  chrome.storage.local.get("check", function (result) {
    if (result.check == null) {
      let value = true
      chrome.storage.local.set({
        'check': value
      }, function () {
        console.log('Value is set to ' + value);
      });
    }
    else {
      console.log(result.check)
      check.checked = result.check
    }
  });

  // let ans;

  // chrome.storage.local.get("check", function (result) {
  //   ans = result.check
  // });

  // if (ans) {
  //   value = true
  //   chrome.storage.local.set({
  //     'check': value
  //   }, function () {
  //     console.log('Value is set to ' + value);
  //     check.checked = true
  //   });
  // } else {
  //   value = false
  //   chrome.storage.local.set({
  //     'check': value
  //   }, function () {
  //     console.log('Value is set to ' + value);
  //     check.checked = false
  //   });
  // }
  check.addEventListener("change", () => {
    if (check.checked) {
      console.log("to")
      value = true
      chrome.storage.local.set({
        'check': value
      }, function () {
        console.log('Value is set to ' + value);
        check.checked = true
      });
    } else {
      value = false
      chrome.storage.local.set({
        'check': value
      }, function () {
        console.log('Value is set to ' + value);
        check.checked = false
      });
    }
  })

  btn.addEventListener('click', (event) => {
    console.log("hey")
    chrome.tabs.executeScript(null, {
      file: 'content.js',
    });
    chrome.runtime.sendMessage({
      clicked: true
    });
  });