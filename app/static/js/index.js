// window.onload = () => {
//     const delete_buttons = document.querySelectorAll('button[type = delete_]');

// }

function delete_item(id){
    var item_id = id.match(/\d+$/)[0];
    console.log(item_id)
    var data = {"id": item_id};
    $.ajax({
        type: 'POST',
        contentType: 'application/json',
        url: '/tasks/del_task',
        dataType : 'json',
        data : JSON.stringify(data),
        success: function(req) {
            console.log('DONE!');
            console.log(req)
            location.href=location.href;
        }
        
    });
}

