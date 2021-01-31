$(document).ready( function () {
    // 팝업 초기화
    $('.btn-example').click(function(){
        var $href = $(this).attr('href');
        layer_popup($href);
    });

    // 영역 밖으로 클릭시 팝업 종료
    $(document).mouseup(function (e){

        var LayerPopup = $("#layer1");

        var $el = $(LayerPopup);    //레이어의 id를 $el 변수에 저장
        var isDim = $el.prev().hasClass('dimBg'); //dimmed 레이어를 감지하기 위한 boolean 변수
    
        // isDim ? $('.dim-layer').fadeIn() : $el.fadeIn();

        if(LayerPopup.has(e.target).length === 0){
            if(LayerPopup.css('display') == 'block'){
                isDim ? $('.dim-layer').fadeOut() : $el.fadeOut(); // 영역 밖을 클릭하면 레이어가 닫힌다.
                return false;
            }
        }
      });
});
function layer_popup(el){
    var $el = $(el);    //레이어의 id를 $el 변수에 저장
    var isDim = $el.prev().hasClass('dimBg'); //dimmed 레이어를 감지하기 위한 boolean 변수

    isDim ? $('.dim-layer').fadeIn() : $el.fadeIn();

    var $elWidth = ~~($el.outerWidth()),
        $elHeight = ~~($el.outerHeight()),
        docWidth = $(document).width(),
        docHeight = $(document).height();


    // 화면의 중앙에 레이어를 띄운다.
    if ($elHeight < docHeight || $elWidth < docWidth) {
        $el.css({
            marginTop: -$elHeight /2,
            marginLeft: -$elWidth/2
        })
    } else {
        $el.css({top: 0, left: 0});
    }

    $el.find('a.btn-layerClose').click(function(){
        isDim ? $('.dim-layer').fadeOut() : $el.fadeOut(); // 닫기 버튼을 클릭하면 레이어가 닫힌다.
        return false;
    });

    $('.layer .dimBg').click(function(){
        $('.dim-layer').fadeOut();
        return false;
    });

}