$(function(){


    var AppRouter = Backbone.Router.extend({


        routes: {
            "": "both",
            "students/": "studentsList",
            "students/delete/:id": "studentDelete",
            "students/edit/:id": "studentEdit",
            "students/add": "studentAdd",

            "groups": "groupsList",
            "groups/delete/:id": "groupDelete",
            "groups/edit/:id": "groupEdit",
            "groups/add": "groupAdd"

        },
        both: function(){
            group_view.initialize("list");
            student_view.initialize("list");
        },

        studentsList: function(){
            student_view.initialize("list")
        },

        studentDelete: function(id){
            student_view.initialize("delete", id);
        },

        studentEdit: function(id){
            student_view.initialize("edit", id)
        },

        studentAdd: function(){
            student_view.initialize("add")
        },

        groupsList: function(){
            group_view.initialize("list")
        },

        groupDelete: function(id){
            group_view.initialize("delete", id);
        },

        groupEdit: function(id){
            group_view.initialize("edit", id)
        },

        groupAdd: function(){
            group_view.initialize("add")
        }

    });

    var student_view = new StudentView({"id":0});
    var group_view = new GroupView({"id":0});

    var router = new AppRouter();

    Backbone.history.start({ root: "/aj/"});

});
