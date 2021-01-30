var lang_kor = {
    "decimal": "",
    "emptyTable": "데이터가 없습니다.",
    "thousands": ",",
    "lengthMenu": "_MENU_ 개 씩 보기",
    "loadingRecords": "로딩중...",
    "processing": "처리중...",
    "search": "검색 : ",
    "zeroRecords": "검색된 데이터가 없습니다.",
    "paginate": {
        "first": "첫 페이지",
        "last": "마지막 페이지",
        "next": "다음",
        "previous": "이전"
    },
    "aria": {
        "sortAscending": " :  오름차순 정렬",
        "sortDescending": " :  내림차순 정렬"
    }
};

$(document).ready(function () {
    $('#dataTable').DataTable({
        "language": lang_kor,
        "paging": true,
        "filter": true,
        "info": false,
        "order": [[4, "desc"]],
    });
});
