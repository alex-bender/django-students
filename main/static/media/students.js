$(function(){

    Student = Backbone.Model.extend({

        urlRoot: "/api/students",
        idAttribute: "id",
        defaults: {
            "id": null,
            "name": null
        },

        validate: function(){
            if (this.attributes.name == null){
                return "Name must not be a null";
            }
        },
        url: function(){
            var id = this.get(this.idAttribute);
            if (id == null) {
                return this.urlRoot+'/';
            }else{
                return this.urlRoot+'/'+this.get(this.idAttribute)+'/';
            }
        }
    });


    StudentCollection =  Backbone.Collection.extend({

        model : Student,
        url : "/api/students/.json",

        initialize: function(){
        },
        parse: function (resp, xhr) {
            return resp.results;
        }
    });

    StudentView = Backbone.View.extend({

        id: 0,
        state: "",
        el: '#students',

        initialize: function(state, id){
            console.log('student view init');
            this.id = id;
            this.state = state;
            this.render(state, id);
        },

        render: function(state, id){
            var student = new Student({"id":id});
            var students = new StudentCollection();
            var groups = new GroupCollection();
            var student_template = $("#student").html();

            if (state=="list"){
               this.id = false;
                students.fetch({
                    success: function(){

                        var template = Handlebars.compile(student_template);
                        var context = {"students": students.toJSON()};
                        var html = template(context);
                        $("#students").html(html);
                        $('#students').append(
            '<a href="#students/add" class="button green" id="student_add">Add</a>'
                        )
                    }
                });
            }
            else if(state=="edit"){

                var context = {};
                student.id = id;
                student.fetch({
                    success: function(){
                        groups.fetch({
                            success: function(){
                                context = {
                                    "student": student.toJSON(),
                                    "groups": groups.toJSON()
                                };
                                var edit_form = $("#student-edit-form").html();
                                var template = Handlebars.compile(edit_form);
                                var html = template(context);
                                $("#students").html(html);
                            }
                        });
                    }
                });
            }

            else if(state == "delete"){

                $(this.el).html('<div class="add">' +
                    '<a href="'+this.id+'"class="button red" id="student_delete">' +
                    'Delete</a></div>'
                );

            }
            else if(state=="add"){

                delete(student.id);
                groups.fetch({
                        success: function(){
                            var edit_form = $("#student-edit-form").html();
                            context = {"groups":groups.toJSON()};
                            var template = Handlebars.compile(edit_form);
                            var html = template(context);
                            $("#students").html(html);
                        }
                    }
                );
                $("a#student_edit.button.purple").detach();
            }
        },

        events: {
            'click a#student_save.button.purple': 'editStudent',
            'click a#student_delete.button.red': 'deleteStudent'
        },

        editStudent: function(e){

            e.stopPropagation();
            var self = this;
            var id = $(e.currentTarget).attr('href');
            var student;
            if (!id){
                student = new Student();
            }else{
                student = new Student({"id":id});
            }

            var frm = $("form#edit_student.myform");
            var ara = frm.serializeArray();
            var data = {};
            $.each(ara, function(i, val){
                data[val.name] = val.value;
            });
            student.save(data, {
                success: function(){
                    self.render("list")
                }
            });
            return false;
        },
        deleteStudent: function(e){
            e.stopPropagation();
            var id = $(e.currentTarget).attr('href');
            var self = this;
            var student = new Student({"id":id});
            student.destroy({
                success: function(){
                    self.render("list")
                }
            });
            return false;
        }
    });

});