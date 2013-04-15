$(function(){


    window.Group = Backbone.Model.extend({
        urlRoot: "/api/groups",
        idAttribute: "id"
    });


    window.Groups = Backbone.Collection.extend({
        model:Group,
        urlRoot:"/api/groups"
    });

    $("#grp").keyup(function () {
        var value = $(this).val();
        $("p").text(value);
    }).keyup();

    gr1 = new window.Group({"id":1});

    $("#ftch").click(function() {
        gr1.fetch();
        console.log(gr1.get('id')+' '+gr1.get('name'));
    });

    var GroupCollection =  Backbone.Collection.extend({
        model : Group
    });

    var ListGroups = new GroupCollection();

    ListGroups.on("add", function(group) {
        console.log(group.get("name")+' '+'added');
    });
    debugger;
    ListGroups.add([
        {"url": "http://127.0.0.1:8000/api/groups/1/.json", "name": "first", "senior": null},
        {"url": "http://127.0.0.1:8000/api/groups/2/.json", "name": "zero", "senior": null}
    ]);

    //ListGroups.models[1].get('name')

    var group1 = ListGroups.get(1);
    console.log(group1);
    $.lalala = 12;
});

