  // popup script
  let btn = document.querySelector(".btn")
  console.log(btn)
  let check = document.querySelector(".check")
  console.log(check)
  check.addEventListener("change", () => {
    if (check.checked) {
      console.log("to")
      localStorage["check"] = true
    } else {
      localStorage["check"] = false
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