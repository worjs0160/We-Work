$(document).ready(function () {
    $('#doc_select').change(function () {
        alert("asd");
        var doc_type = $(this).val();
        $('.view_box').children().remove();
        $('#doctype').val(doc_type);
        $('#create').attr("style", "display:inline");
        $('#submit').attr("style", "display:none");
        $('.view_box').load('doc_format/' + doc_type + '.html');
        return false;
    });

    $('#new_doc').click(function () {
        /*새 문서 작성*/
        $(".approval-body").children().remove();
        $(".approval-body").load('new_doc');
        return false;
    });

    $('#create').click(function () {
        /*글쓰기*/
        $('.input').attr({
            "readonly": false,
            "disabled": false,
        });
        $('#submit').attr("style", "display:inline");
        $('#create').attr("style", "display:none");
        return false;
    });
});