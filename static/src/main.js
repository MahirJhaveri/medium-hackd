
// checks if url is valid and belongs to medium.com
function verify_and_parse_url(url) {
    var regexp = /^https:\/\/(.+)\/(.+)$/;
    var result = url.match(regexp);
    if (result == null) {
        return null
    }
    else {
        domain = result[1];
        path = result[2];
        new_url = "http://localhost:5000/" + domain + "/" + path;
        return new_url;
    }
}

// retrieves the medium.com article
function load_article(new_url) {
    window.location.href = new_url;
}

// Update the page to display the medium.com article
function update_display() { }

$(document).ready(
    function () {
        $('#send').click(function () {
            var input = $('#textbox').val();
            var new_url = verify_and_parse_url(input);
            if (new_url) {
                load_article(new_url);
            }
            else {
                console.log("Invalid url please try again");
            }
        });

        $('#textbox').keyup(function (event) {
            if (event.keyCode === 13) {
                $("#send").click();
            }
        });
    }
);