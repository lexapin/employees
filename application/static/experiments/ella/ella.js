var me = {};
me.avatar = "man.png";

var ella = {};
ella.avatar = "ella.jpg";

function formatAMPM(date) {
    var hours = date.getHours();
    var minutes = date.getMinutes();
    var ampm = hours >= 12 ? 'PM' : 'AM';
    hours = hours % 12;
    hours = hours ? hours : 12; // the hour '0' should be '12'
    minutes = minutes < 10 ? '0'+minutes : minutes;
    var strTime = hours + ':' + minutes + ' ' + ampm;
    return strTime;
}            


function insertChat(who, text, time = 0){
    var control = "";
    var date = formatAMPM(new Date());
    
    if (who == "me"){
        
        control = '<li style="width:100%">' +
                        '<div class="msj macro">' +
                        '<div class="avatar"><img class="img-circle" style="width:100%;" src="'+ me.avatar +'" /></div>' +
                            '<div class="text text-l">' +
                                '<p>'+ text +'</p>' +
                                '<p><small>'+date+'</small></p>' +
                            '</div>' +
                        '</div>' +
                    '</li>';                    
    }else{
        control = '<li style="width:100%;">' +
                        '<div class="msj-rta macro">' +
                            '<div class="text text-r">' +
                                '<p>'+text+'</p>' +
                                '<p><small>'+date+'</small></p>' +
                            '</div>' +
                        '<div class="avatar" style="padding:0px 0px 0px 10px !important"><img class="img-circle" style="width:100%;" src="'+ella.avatar+'" /></div>' +                                
                  '</li>';
    }
    setTimeout(
        function(){                        
            $("ul").append(control);

        }, time);
    
}

function resetChat(){
    $("ul").empty();
}

$(".mytext").on("keyup", function(e){
    if (e.which == 13){
        var text = $(this).val();
        if (text !== ""){
            insertChat("me", text);   
            insertChat("ella", get_ella_response(), 1000)           
            $(this).val('');
        }
    }
});

function get_ella_response(){
    var ella_says = [
        "Хамите.",
        "Хо-хо!",
        "Знаменито.",
        "Мрачный.",
        "Мрак.",
        "Жуть.",
        "Парниша.",
        "Не учите меня жить.",
        "Как ребёнка.",
        "Кр-р-расота!",
        "Толстый и красивый.",
        "Поедем на извозчике.",
        "Поедем на таксо ",
        "У вас вся спина белая.",
        "Подумаешь!",
        "Уля.",
        "Ого!",
    ]
    return ella_says[Math.floor(Math.random() * ella_says.length)];
}


resetChat();

