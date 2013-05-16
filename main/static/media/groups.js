$(function(){

    Group = Backbone.Model.extend({

        urlRoot: "/api/groups",
        idAttribute: "id",
        defaults: {
            "id": null,
            "name": null
        },

        validate: function(attrs){
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

    GroupCollection =  Backbone.Collection.extend({

        model : Group,
        url: "/api/groups/.json",
        initialize: function(){
        },
        parse: function (resp, xhr) {
            return resp.results;
        }

    });

    GroupView = Backbone.View.extend({

        id: 0,
        state: "",
        el: '#groups',

        initialize: function(state, id){
            console.log('group view init');
            this.id = id;
            this.state = state;
            this.render(state, id);
        },

        render: function(state, id){
            var group = new Group({"id":id});
            var groups = new GroupCollection();
            var students = new StudentCollection();
            var group_template = $("#group").html();

            if(state=="list"){
                this.id = false;
                 groups.fetch({
                    success: function(){

                        var template = Handlebars.compile(group_template);
                        var context = {"groups": groups.toJSON()};
                        var html = template(context);
                        $("#groups").html(html);
                        $('#groups').append(
                            '<a href="#groups/add" class="button green" id="group_add">Add</a>'
                        )
                    }
                });
            }
            else if(state=="edit"){

                var context = {};
                group.id = id;
                group.fetch({
                    success: function(){
                        students.fetch({
                            success: function(){
                                context = {
                                    "group": group.toJSON(),
                                    "students": students.toJSON()
                                };
                                var edit_form = $("#group-edit-form").html();
                                var template = Handlebars.compile(edit_form);
                                var html = template(context);
                                $("#groups").html(html);

                            }
                        });
                    }
                });
//                return false;

            }else if(state == "delete"){
                $(this.el).html('<div class="add">' +
                    '<a href="'+this.id+'"class="button red" id="group_delete">' +
                    'Delete</a></div>'
                );
            }else if(state == "add"){

                delete(group.id);
                students.fetch({
                    success: function(){
                        var edit_form = $("#group-edit-form").html();
                        context = {"students": students.toJSON()};
                        var template = Handlebars.compile(edit_form);
                        var html = template(context);
                        $("#groups").html(html);
                        }
                    }
                );
                $("a#groups_edit.button.purple").detach(); // ????

            }
        },

        events: {
            'click a#group_save.button.purple': 'editGroup',
            'click a#group_delete.button.red': 'deleteGroup'
        },

        editGroup: function(e){

            e.stopPropagation();
            var self = this;
            var id = $(e.currentTarget).attr('href');
            var group;
            if(!id){
                group = new Group();
            }else{
                group = new Group({"id":id});
            }

            var frm = $("form#edit_group.myform");
            var ara = frm.serializeArray();
            var data = {};
            $.each(ara, function(i, val){
                data[val.name] = val.value;
            });
            group.save(data, {
                success: function(){
                    self.render("list")
                }
            });
            return false;
        },
        deleteGroup: function(e){
            e.stopPropagation();
            var id = $(e.currentTarget).attr('href');
            var self = this;
            var group = new Group({"id":id});
            group.destroy({
                success: function(){
                    self.render("list")
                }
            });
            return false
        }
    });
});