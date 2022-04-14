var item_info = $("#item_info")
function sendItemId(id) {
    $.ajax({
        type: "POST",
        url: `/companies/{{company.id}}/`,
        data: JSON.stringify(id),
        success: function (json) {
            data = JSON.parse(json);
            item = data[0]["fields"];
            console.log(item);
            $(item_info).append("<h4> 이름 : " + item["name"] + "</h4>");
            $(item_info).append("<p> 온도 : " + item["temperature"] + "</p>");
        },
        error: function (xhr, errmsg, err) {
            console.log(err);
        },
    });
}
function getItemInfo(id) {
    sendItemId(id)
}