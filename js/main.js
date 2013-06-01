function readjust() {
    var myOptions = {
        center: new google.maps.LatLng(38.905024, -98.677202),
        zoom: 5,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    };
    var map = new google.maps.Map(document.getElementById("map_canvas"),
    myOptions);
    var vafacilities = new google.maps.FusionTablesLayer({
        query: {
            select: 'G_LAT',
            from: '3855490'
        },
    });
    var POPm = new google.maps.FusionTablesLayer({
        query: {
            select: 'geometry',
            from: '3856224'
        },
    });
    var VHAm = new google.maps.FusionTablesLayer({
        query: {
            select: 'G_LAT',
            from: '3855490',
            where: 'VAadmin_mapcode = 1'
        }
    });
    var VBAm = new google.maps.FusionTablesLayer({
        query: {
            select: 'G_LAT',
            from: '3855490',
            where: 'VAadmin_mapcode = 2'
        }
    });
    var NCAm = new google.maps.FusionTablesLayer({
        query: {
            select: 'G_LAT',
            from: '3855490',
            where: 'VAadmin_mapcode = 3'
        }
    });
    if (document.getElementById("POPc").checked == true) {
        POPm.setMap(map);
    } else {
        "";
    }
    if (document.getElementById("VHAc").checked == true) {
        VHAm.setMap(map);
    } else {
        "";
    }
    if (document.getElementById("VBAc").checked == true) {
        VBAm.setMap(map);
    } else {
        "";
    }
    if (document.getElementById("NCAc").checked == true) {
        NCAm.setMap(map);
    } else {
        "";
    }
}

function searchrun() {
    $(".content_div").hide();
    $("#tab_search_results").show();
    $("#loader_gif").show();
    $(".tab").toggleClass("mytab_selected", false);
    $(".tab").toggleClass("mytab_unselected", true);
    $("#tab_search_results").toggleClass("mytab_unselected", false);
    $("#tab_search_results").toggleClass("mytab_selected", true);
    var selectors = $(".source_selector");
    var checked_vals = '';
    for (var i = 0; i < selectors.length; i++) {
        checked_vals += selectors[i].checked + ",";
    }
    // document.write(checked + ",");
    var date_from = $("#datepicker_from").val();
    var date_to = $("#datepicker_to").val();
    var search_term = $("#search_term_input").val();
    var datastring = "search_term=" + search_term + "&date_from=" + date_from + "&date_to=" + date_to + "&checked_vals=" + checked_vals;
    $.ajax({
        url: "/search_results",
        data: datastring,
        dataType: "html",
        success: (function (data) {
            $("#search_content").html(data);
            $("#loader_gif").hide();
            $("#search_content").show();
        })
    })
}

function enterpress(e) {
    if (e.keyCode == 13) {
        searchrun();
    } else {
        return false;
    }
}

function resort() {
    if ($("#resort_score").attr("selected") == "selected") {
        datastring = $("#resort_score").attr("name")
    } else if ($("#resort_d_desc").attr("selected") == "selected") {
        datastring = $("#resort_d_desc").attr("name")
    } else if ($("#resort_d_asc").attr("selected") == "selected") {
        datastring = $("#resort_d_asc").attr("name")
    }
    $.ajax({
        url: "/resort",
        data: datastring,
        dataType: "html",
        success: (function (data) {
            $("#s_results_table").html(data);
        })
    });
    $(".show_more").hide();
    $("#po_side").hide();
    $("#po_side").hide();
}
// $("#resort").live("click", function (event) {
// var datastring = $(this).attr("name")
// $.ajax({
// url: "/resort",
// data: datastring,
// dataType: "html",
// success: (function (data) {
// $("#search_rows").html(data);
//
// })
// })
// $(".show_more").hide();
// $("#po_side").hide();
// $("#po_side").hide();
// });
$(function () {
    $("#datepicker_from").datepicker();
    $("#format").change(function () {
        $("#datepicker").datepicker("option", "dateFormat", $(this).val());
    });
});
$(function () {
    $("#datepicker_to").datepicker();
    $("#format").change(function () {
        $("#datepicker").datepicker("option", "dateFormat", $(this).val());
    });
});

function db_save() {
    var ID = $("#save_button").attr('name');
    var title = encodeURIComponent($("#title_" + ID).val());
    var description = encodeURIComponent($("#description_" + ID).val());
    var relevance = encodeURIComponent($("#relevance_" + ID).val());
    var tags = encodeURIComponent($("#tags_" + ID).val());
    var origin = encodeURIComponent($("#origin_" + ID).val());
    var issue = encodeURIComponent($("#issue_" + ID).val());
    var format = encodeURIComponent($("#format_" + ID).val());
    var policy = encodeURIComponent($("#policy_" + ID).val());
    var wrcheck = $("#wr_check_" + ID).attr('checked');
    var reposcheck = $("#repos_check_" + ID).attr('checked');
    var esil_select = $("#esil_select_" + ID).val();
    var c = $("#code_" + ID).val();
    var dataString = "ID=" + ID + "&tags=" + tags + "&origin=" + origin + "&issue=" + issue + "&format=" + format + "&policy=" + policy + "&title=" + title + "&description=" + description + "&relevance=" + relevance + "&wrcheck=" + wrcheck + "&reposcheck=" + reposcheck + "&esil_select=" + esil_select + "&c=" + c;
    $.ajax({
        url: "/db_save",
        type: "POST",
        data: dataString,
        dataType: "html",
        error: function () {
            $("#update_stamp").html("Save Failed, Try Again");
        },
        success: function (data) {
            $("#update_stamp").html(data);
            if (data == "Saved!" && $("#row_" + ID)[0]) {
                $.ajax({
                    url: "/repost",
                    data: dataString,
                    dataType: "html",
                    success: function (data) {
                        $("#row_" + ID).html(data);
                    }
                });
            }
            if (data == "Saved!" && $("#list_" + ID)[0]) {
                $.ajax({
                    url: "/repost_list",
                    data: dataString,
                    dataType: "html",
                    success: function (data) {
                        $("#list_" + ID).html(data);
                    }
                });
            }
        }
    });
};

function modcloser() {
    document.getElementById('mod_content').innerHTML = '';
    document.getElementById('mod_content2').innerHTML = '';
};
$(".cbox").live("click", function (event) {
    var selector_name = $(this).attr("name");
    if ($("#" + selector_name + "_fields").hasClass("checked")) {
        $("#" + selector_name + "_fields").toggleClass("checked", false);
        $("#" + selector_name + "_fields").toggleClass("unchecked", true);
    } else {
        $("#" + selector_name + "_fields").toggleClass("checked", true);
        $("#" + selector_name + "_fields").toggleClass("unchecked", false);
    };
});
$("#delete_record").live("click", function (event) {
    var d_key = $(this).attr("name");
    var c = $("#code_" + d_key).val();
    var dataString = "d_key=" + d_key + "&c=" + c;
    var confirm_message = "Are you sure you want to delete this record?"
    if (confirm(confirm_message)) {
        $.ajax({
            url: "/deleterecord",
            data: dataString,
            dataType: "html",
            success: (function (data) {
                if (data == "good") {
                    $("#list_" + d_key).hide();
                    $("#row_" + d_key).hide();
                    document.getElementById('database_editor').innerHTML = '';
                } else {
                    $("#update_stamp").html(data);
                }
            })
        })
    } else {
        return false
    }
});

$(document).on("click", ".nw_link",  function (event) {
    var this_url = $(this).attr('href')    
//    window.open(this_url)
    var ajax_link = "/cl?p=mp&l=" + encodeURIComponent(this_url);
    $.ajax({
url: ajax_link, success: (function () {return false}) });
});





$(document).ready(function () {
    // $(function () {
    // $('#mod_content').jqm({
    // trigger: 'a.modTrigger',
    // ajax: '@href',
    // /* Extract ajax URL from the 'href' attribute of triggering element */
    // modal: true,
    // // onHide: modcloser,
    // // target: t,
    // // overlay: 0
    // });
    // });
    $(".modTrigger2").live("click", function (event) {
        var ref = $(this).attr('name');
        $.ajax({
            url: ref,
            dataType: "html",
            success: function (data) {
                $('#mod_content2').html(data);
                $('#mod_content2').jqm({
                    modal: true,
                    // onHide: modcloser,
                });
                $('#mod_content2').jqmShow();
            }
        });
    });
    $(".tab").click(function () {
        var this_content_box = $(this).attr('name');
        var this_id = $(this).attr('id');
        $(".tab").toggleClass("mytab_selected", false);
        $(".tab").toggleClass("mytab_unselected", true);
        $(this).toggleClass("mytab_unselected", false);
        $(this).toggleClass("mytab_selected", true);
        if (this_id == "tab_facilities_map") {
            $.ajax({
                url: "/map",
                dataType: "html",
                success: (function (data) {
                    $("#map_content").html(data)
                    readjust();
                })
            });
        }
        $(".content_div").hide();
        $("#" + this_content_box).show();
    });
    $("#submit_button").click(function () {
        searchrun();
    })
    $("#advanced_selector").click(function () {
        var av_search_box = document.getElementById("advanced_search");
        var av_toggle = document.getElementById("advanced_selector");
        if (av_search_box.style.display == "block") {
            av_search_box.style.display = "none";
            av_toggle.innerHTML = "Show Advanced...";
        } else {
            av_search_box.style.display = "block";
            av_toggle.innerHTML = "Hide Advanced...";
        }
    })
    $("#delete_selected").click(function () {
        var node_list = document.getElementsByTagName("input");
        var ids = new Array;
        for (var i = 0; i < node_list.length; i++) {
            var node = node_list[i];
            if (node.checked == true) {
                // do something here with a <input type="text" .../>
                // we alert its value here
                var ID = node.getAttribute('id');
                ids.push(ID)
            }
        }
        var dataString = "ids=" + ids
        $.ajax({
            url: "/df",
            data: dataString,
            dataType: "html",
            success: (function (data) {
                $("#feeds_list").html(data)
            })
        })
    })
    $(".item_row").live({
        mouseover: function () {
            elem = $(this);
            if (elem.hasClass("row_white")) {
                $(this).removeClass("row_white");
                bcol = "w"
            };
            if (elem.hasClass("row_blueish")) {
                $(this).removeClass("row_blueish");
                bcol = "b"
            };
            $(this).addClass("row_hover");
        },
        mouseout: function () {
            $(this).removeClass("row_hover");
            if (bcol == "w") {
                $(this).addClass("row_white")
            }
            if (bcol == "b") {
                $(this).addClass("row_blueish")
            }
        }
    });
    $(".pageover").live("click", function (event) {
        var datastring = $(this).attr("name")
        $.ajax({
            url: "/p",
            data: datastring,
            dataType: "html",
            success: (function (data) {
                $("#home_content").append(data);
            })
        })
        $(this).hide();
        $("#po_side").hide();
        $("#po_side").hide();
    });
    $(".more_results").live("click", function (event) {
        var datastring = $(this).attr("name")
        $.ajax({
            url: "/r",
            data: datastring,
            dataType: "html",
            success: (function (data) {
                $("#search_rows").append(data);
            })
        })
        $(this).hide();
        $("#po_side").hide();
        $("#po_side").hide();
    });
});