$(window).on('load', function () {
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

    $('#my_doc').click(function () {
        /*내 문서 들어가기*/
        $(".approval-body").children().remove();
        $(".approval-body").load('my_doc_list');
        return false;
    });

    $('#view_doc').click(function () {
        /*열람 가능 문서 들어가기*/
        $(".approval-body").children().remove();
        $(".approval-body").load('view_doc_list');
        return false;
    });

    $('#approval_doc').click(function () {
        /*결재함 들어가기*/
        $(".approval-body").children().remove();
        $(".approval-body").load('approval_doc_list');
        return false;
    });

    $('#detail').click(function () {
        /*문서 열람페이지 들어가기*/
        $(".approval-body").children().remove();
        $(".approval-body").load('detail');
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