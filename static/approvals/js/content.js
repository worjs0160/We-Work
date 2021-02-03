$('.table_item').click(function(){
    
    var input = $(this)[0].innerText;
    if(input == "기안서"){
        $('.view_box').children().remove();
        var paper_item = '<div class="m_right5 m_left5">'+
            '<!-- s: 폼 양식명 -->'+
            '<div class="view_title_box" style="word-break:break-all;">기안서</div>'+
            '<!-- e: 폼 양식명 -->'+
            '<!-- s: 공통 양식 테이블-->'+
            '<table class="basic_table type_e m_bottom15 a4_size" cellpadding="0" cellspacing="0">'+
                '<colgroup><col width="120px"><col width="*"></colgroup>'+
                '<tbody>'+
                    '<tr>'+
                        '<th>제목</th>'+ 
                        '<!-- 제목 -->'+
                        '<td colspan="3">'+
                            '<span> 기안서 </span>'+
                        '</td>'+
                    '</tr>'+
                    '<tr>'+
                        '<th>열람/공람자</th> <!-- 열람/공람자 -->'+
                        '<td colspan="3" class="fix_height">'+
                        '</td>'+
                    '</tr>'+
                '</tbody>'+
            '</table>   '+ 
        '</div>'+
        '<textarea>내용 작성(에디터)</textarea>';
        $('.view_box').append(paper_item);
    }
    if(input == "지출결의서"){
        $('.view_box').children().remove();
        var paper_item = '<div class="m_right5 m_left5">'+
            '<!-- s: 폼 양식명 -->'+
            '<div class="view_title_box" style="word-break:break-all;">지출결의서</div>'+
            '<!-- e: 폼 양식명 -->'+
            '<!-- s: 공통 양식 테이블-->'+
            '<table class="basic_table type_e m_bottom15 a4_size" cellpadding="0" cellspacing="0">'+
                '<colgroup><col width="120px"><col width="*"></colgroup>'+
                '<tbody>'+
                    '<tr>'+
                        '<th>제목</th>'+ 
                        '<!-- 제목 -->'+
                        '<td colspan="3">'+
                            '<span> 지출결의서 </span>'+
                        '</td>'+
                    '</tr>'+
                    '<tr>'+
                        '<th>열람/공람자</th> <!-- 열람/공람자 -->'+
                        '<td colspan="3" class="fix_height">'+
                        '</td>'+
                    '</tr>'+
                '</tbody>'+
            '</table>   '+ 
            '<table class="basic_table type_e m_bottom15 a4_size" cellpadding="0" cellspacing="0">'+
                '<colgroup>'+
                    '<col width="120px">'+
                    '<col width="*">'+
                    '<col width="120px">'+
                    '<col width="*">'+
                    '<col width="120px">'+
                    '<col width="*">'+
                    '</colgroup>'+
                    '<tbody>'+
                        '<tr>'+
                            '<th>사용부서</th>'+
                            '<td colspan="2" class="in_button">'+
                                '<input class="input_box" type="text" name="[]" id="_double_0" readonly="readonly" disabled="disabled">'+
                                '</td>'+
                                '<th>사용자</th>'+
                                '<td colspan="2" class="in_button">'+
                                    '<input class="input_box" type="text" name="[]" id="_double_1" readonly="readonly" disabled="disabled">'+
                                    '</td>'+
                                    '</tr>'+
                                    '</tbody>'+
                                    '</table>'+
        '</div>'+
        '<textarea>내용 작성(에디터)</textarea>';
        $('.view_box').append(paper_item);
    }
    
    if(input == "결과보고서"){
        $('.view_box').children().remove();
        var paper_item = '<div class="m_right5 m_left5">'+
            '<!-- s: 폼 양식명 -->'+
            '<div class="view_title_box" style="word-break:break-all;">결과보고서</div>'+
            '<!-- e: 폼 양식명 -->'+
            '<!-- s: 공통 양식 테이블-->'+
            '<table class="basic_table type_e m_bottom15 a4_size" cellpadding="0" cellspacing="0">'+
                '<colgroup><col width="120px"><col width="*"></colgroup>'+
                '<tbody>'+
                    '<tr>'+
                        '<th>제목</th>'+ 
                        '<!-- 제목 -->'+
                        '<td colspan="3">'+
                            '<span> 결과보고서 </span>'+
                        '</td>'+
                    '</tr>'+
                    '<tr>'+
                        '<th>열람/공람자</th> <!-- 열람/공람자 -->'+
                        '<td colspan="3" class="fix_height">'+
                        '</td>'+
                    '</tr>'+
                '</tbody>'+
            '</table>   '+ 
        '</div>'+
        '<textarea>내용 작성(에디터)</textarea>';
        $('.view_box').append(paper_item);
    }
    
    
    if(input == "휴가신청서"){
        $('.view_box').children().remove();
        var paper_item = '<div class="m_right5 m_left5">'+
            '<!-- s: 폼 양식명 -->'+
            '<div class="view_title_box" style="word-break:break-all;">휴가신청서</div>'+
            '<!-- e: 폼 양식명 -->'+
            '<!-- s: 공통 양식 테이블-->'+
            '<table class="basic_table type_e m_bottom15 a4_size" cellpadding="0" cellspacing="0">'+
                '<colgroup><col width="120px"><col width="*"></colgroup>'+
                '<tbody>'+
                    '<tr>'+
                        '<th>제목</th>'+ 
                        '<!-- 제목 -->'+
                        '<td colspan="3">'+
                            '<span> 휴가신청서 </span>'+
                        '</td>'+
                    '</tr>'+
                    '<tr>'+
                        '<th>열람/공람자</th> <!-- 열람/공람자 -->'+
                        '<td colspan="3" class="fix_height">'+
                        '</td>'+
                    '</tr>'+
                '</tbody>'+
            '</table>   '+ 
            '<table class="basic_table type_e m_bottom15 a4_size" cellpadding="0" cellspacing="0">'+ 
                '<colgroup>'+ 
                    '<col width="120px">'+ 
                    '<col width="*">'+ 
                    '<col width="120px">'+ 
                    '<col width="*">'+ 
                    '<col width="120px">'+ 
                    '<col width="*">'+ 
                    '</colgroup>'+ 
                '<tbody>'+ 
                    '<tr>'+ 
                        '<th>휴가 종류</th>'+ 
                        '<td class="in_button" colspan="2">'+ 
                            '<select class="select_box select2-hidden-accessible" name="" id="" disabled="" tabindex="-1" aria-hidden="true">'+ 
                                '<option value="">선택 </option> <!-- 선택 -->'+ 
                                '<option value="2021 연차">2021 연차</option>'+ 
                                '<option value="포상휴가">포상휴가</option>'+ 
                                '<option value="경조휴가">경조휴가</option>'+ 
                                '<option value="생리휴가">생리휴가</option>'+ 
                                '<option value="기타휴가">기타휴가</option>'+ 
                                '</select><span class="select2 select2-container select2-container--lw-classic select2-container--disabled" dir="ltr" style="width: 100%;"><span class="selection"><span class="select2-selection select2-selection--single" role="combobox" aria-haspopup="true" aria-expanded="false" tabindex="-1" aria-labelledby="select2--container"><span class="select2-selection__rendered" id="select2--container" title="선택 ">선택 </span><span class="select2-selection__arrow" role="presentation"><b role="presentation"></b></span></span></span><span class="dropdown-wrapper" aria-hidden="true"></span></span>'+ 
                            '</td>'+ 
                        '<td class="in_button b_left_none" colspan="3">'+ 
                            '<input type="checkbox" class="v_mid_right5" id="chkbox_half" name="chkbox_half" disabled=""> <label for="chkbox_half&quot;"> 반차 사용</label>'+ 
                            '</td>'+ 
                        '</tr>'+ 
                    '<tr>'+ 
                        '<th>'+ 
                            '<span>휴가 기간</span>'+ 
                            '</th>'+ 
                        '<td colspan="5">'+ 
                            '<div id="all_">'+ 
                                '<div class="calender_box">'+ 
                                    '<input class="input_box hasDatepicker" type="text" name="[]" id="_s_date" readonly="readonly" data-plugin="datepicker" data-date="2021-01-31" data-format="yy-mm-dd" data-disabled="disabled" disabled=""><button type="button" class="ui-datepicker-trigger" disabled=""><i class="mdi mdi-calendar-month-outline mdi-20 mdi-500" style="position: relative; z-index: 99;"></i></button>'+ 
                                    '</div>'+ 
                                '<span>~</span>'+ 
                                '<div class="calender_box">'+ 
                                    '<input class="input_box hasDatepicker" type="text" name="[]" id="_e_date" readonly="readonly" data-plugin="datepicker" data-date="2021-01-31" data-format="yy-mm-dd" data-disabled="disabled" disabled=""><button type="button" class="ui-datepicker-trigger" disabled=""><i class="mdi mdi-calendar-month-outline mdi-20 mdi-500" style="position: relative; z-index: 99;"></i></button>'+ 
                                    '</div>'+ 
                                '<div class="inblock">'+ 
                                    '<span>, 총</span><input type="text" class="input_box half" name="[]" id="" value="" readonly="readonly"> 일'+ 
                                    '</div>'+ 
                                '<span style="display:none"><input type="radio" name="_type[]" id="_type_1" value="1" validate="required:true" ename="휴가 기간" checked=""></span>'+ 
                                '</div>	'+ 
                            '<div class="inblock f_right" style="line-height:32px;">'+ 
                                '<input type="checkbox" class="v_mid_left5" id="restore_vac" name="restore_vac" readonly="readonly" value="-1" disabled=""> <label for="restore_vac"> 휴가 복구</label>'+ 
                                '<div class="tooltip_wrap f_right">'+ 
                                    '<span id="tooltip_icon" class="mdi mdi-information-outline mdi-20 mdi-500"></span>'+ 
                                    '<div class="tooltip_box" style="bottom:18px;left:-474px">'+ 
                                        '‧ 잔여휴가일 수는 종결 시점 기준으로 계산됩니다. <br>‧ 휴가 복구를 체크하면 결재 완료 시 신청한 휴가일만큼 복구됩니다.'+ 
                                        '</div>'+ 
                                    '</div>'+ 
                                '</div>'+ 
                            '</td></tr>'+ 
                    '<tr>'+ 
                            '<th>휴가 사유</th>'+ 
                            '<td colspan="5" class="in_button">'+ 
                                '<input class="input_box" type="text" name="[]" id="_single" readonly="readonly" disabled="disabled">'+ 
                                '</td>'+ 
                            '</tr>'+ 
                        '</tbody>'+ 
                '</table>'+ 
        '</div>';
        $('.view_box').append(paper_item);
    }
    
    
    
    
    if(input == "회의보고서"){
        $('.view_box').children().remove();
        var paper_item = '<div class="m_right5 m_left5">'+
            '<!-- s: 폼 양식명 -->'+
            '<div class="view_title_box" style="word-break:break-all;">회의보고서</div>'+
            '<!-- e: 폼 양식명 -->'+
            '<!-- s: 공통 양식 테이블-->'+
            '<table class="basic_table type_e m_bottom15 a4_size" cellpadding="0" cellspacing="0">'+
                '<colgroup><col width="120px"><col width="*"></colgroup>'+
                '<tbody>'+
                    '<tr>'+
                        '<th>제목</th>'+ 
                        '<!-- 제목 -->'+
                        '<td colspan="3">'+
                            '<span> 회의보고서 </span>'+
                        '</td>'+
                    '</tr>'+
                    '<tr>'+
                        '<th>열람/공람자</th> <!-- 열람/공람자 -->'+
                        '<td colspan="3" class="fix_height">'+
                        '</td>'+
                    '</tr>'+
                '</tbody>'+
            '</table>   '+ 
            '<table class="basic_table type_e m_bottom15 a4_size" cellpadding="0" cellspacing="0">'+ 
                '<colgroup>'+ 
                    '<col width="120px">'+ 
                    '<col width="*">'+ 
                    '<col width="120px">'+ 
                    '<col width="*">'+ 
                    '<col width="120px">'+ 
                    '<col width="*">'+ 
                    '</colgroup>'+ 
                '<tbody>'+
                    '<tr>'+ 
                            '<th>회의명</th>'+ 
                            '<td colspan="5" class="in_button">'+ 
                                '<input class="input_box" type="text" name="[]" id="_single" readonly="readonly" disabled="disabled">'+ 
                                '</td>'+ 
                            '</tr>'+ 
                    
                    '<tr>'+ 
                        '<th>회의 일시</th>'+ 
                        '<td class="in_button calender" colspan="5">'+ 
                            '<div class="input_wrap write">'+ 
                                '<div class="calender_box write">'+ 
                                    '<input class="input_box hasDatepicker" type="text" name="[]" id="_s_date" readonly="readonly" data-plugin="datepicker" data-date="2021.01.31" data-disabled="disabled" disabled=""><button type="button" class="ui-datepicker-trigger" disabled=""><i class="mdi mdi-calendar-month-outline mdi-20 mdi-500" style="position: relative; z-index: 99;"></i></button>'+ 
                                    '</div>'+ 
                                    '<span class="calender_tilde write">~</span>'+ 
                                    '<div class="calender_box write">'+ 
                                        '<input class="input_box hasDatepicker" type="text" name="[]" id="_e_date" readonly="readonly" data-plugin="datepicker" data-date="2021.01.31" data-disabled="disabled" disabled=""><button type="button" class="ui-datepicker-trigger" disabled=""><i class="mdi mdi-calendar-month-outline mdi-20 mdi-500" style="position: relative; z-index: 99;"></i></button>'+ 
                                        '</div>'+ 
                                        '<div class="total_day">'+ 
                                            ', 총 <input type="text" class="input_box half" name="[]" id="" readonly="readonly" value=""> 일'+ 
                                            '</div>'+ 
                                            '</div>'+ 
                                            '</td>'+ 
                                            '</tr>'+  
                                            '<tr>'+  
                                                '<th>참석 부서</th>'+  
                                                '<td colspan="2" class="in_button">'+  
                                                        '<input class="input_box" type="text" name="[]" id="_double_0" readonly="readonly" disabled="disabled">'+  
                                                    '</td>'+  
                                                '<th>회의 장소</th>'+  
                                                '<td colspan="2" class="in_button">'+  
                                                        '<input class="input_box" type="text" name="[]" id="_double_1" readonly="readonly" disabled="disabled">'+  
                                                    '</td>'+  
                                                '</tr>'+  
                                    '<th>참석자</th>'+ 
                                    '<td colspan="5" class="in_button">'+ 
                                        '<input class="input_box" type="text" name="[]" id="_single" readonly="readonly" disabled="disabled">'+ 
                                        '</td>'+ 
                                    '</tr>'+ 
                                    '<tr>'+ 
                                            '<th>주요 안건</th>'+ 
                                            '<td colspan="5" class="in_button">'+ 
                                                '<input class="input_box" type="text" name="[]" id="_single" readonly="readonly" disabled="disabled">'+ 
                                                '</td>'+ 
                                            '</tr>'+ 
                                            '<tr>'+ 
                                                    '<th>의결사항</th>'+ 
                                                    '<td colspan="5" class="in_button">'+ 
                                                        '<input class="input_box" type="text" name="[]" id="_single" readonly="readonly" disabled="disabled">'+ 
                                                        '</td>'+ 
                                                    '</tr>'+ 
                                    '<tr>'+ 
                                            '<th>기타사항</th>'+ 
                                            '<td colspan="5" class="in_button">'+ 
                                                '<textarea class="form_textarea preview" name="" id="" readonly="readonly" disabled="disabled" style="height: 100px"></textarea>'+ 
                                                '</td>'+ 
                                            '</tr>'+ 
                        '</tbody>'+ 
                '</table>'+ 
        '</div>';
        $('.view_box').append(paper_item);
    }
    
    if(input == "업무보고서"){
        $('.view_box').children().remove();
        var paper_item = '<div class="m_right5 m_left5">'+
            '<!-- s: 폼 양식명 -->'+
            '<div class="view_title_box" style="word-break:break-all;">업무보고서</div>'+
            '<!-- e: 폼 양식명 -->'+
            '<!-- s: 공통 양식 테이블-->'+
            '<table class="basic_table type_e m_bottom15 a4_size" cellpadding="0" cellspacing="0">'+
                '<colgroup><col width="120px"><col width="*"></colgroup>'+
                '<tbody>'+
                    '<tr>'+
                        '<th>제목</th>'+ 
                        '<!-- 제목 -->'+
                        '<td colspan="3">'+
                            '<span> 업무보고서 </span>'+
                        '</td>'+
                    '</tr>'+
                    '<tr>'+
                        '<th>열람/공람자</th> <!-- 열람/공람자 -->'+
                        '<td colspan="3" class="fix_height">'+
                        '</td>'+
                    '</tr>'+
                '</tbody>'+
            '</table>   '+ 
            '<table class="basic_table type_e m_bottom15 a4_size" cellpadding="0" cellspacing="0">'+ 
                '<colgroup>'+ 
                    '<col width="120px">'+ 
                    '<col width="*">'+ 
                    '<col width="120px">'+ 
                    '<col width="*">'+ 
                    '<col width="120px">'+ 
                    '<col width="*">'+ 
                    '</colgroup>'+ 
                '<tbody>'+
                                                '<tr>'+ 
                                                        '<th>금일 업무 목표</th>'+ 
                                                        '<td colspan="5" class="in_button">'+ 
                                                            '<textarea class="form_textarea preview" name="" id="" readonly="readonly" disabled="disabled" style="height: 100px"></textarea>'+ 
                                                            '</td>'+ 
                                                        '</tr>'+ 
                                                        '<tr>'+ 
                                                            '<th>금주 업무 목표</th>'+ 
                                                            '<td colspan="5" class="in_button">'+ 
                                                                '<textarea class="form_textarea preview" name="" id="" readonly="readonly" disabled="disabled" style="height: 100px"></textarea>'+ 
                                                                '</td>'+ 
                                                            '</tr>'+ 
                                                            '<tr>'+ 
                                                                '<th>전일 실시사항</th>'+ 
                                                                '<td colspan="5" class="in_button">'+ 
                                                                    '<textarea class="form_textarea preview" name="" id="" readonly="readonly" disabled="disabled" style="height: 100px"></textarea>'+ 
                                                                    '</td>'+ 
                                                                '</tr>'+ 
                                                                '<tr>'+ 
                                                                    '<th>금일 예정사항</th>'+ 
                                                                    '<td colspan="5" class="in_button">'+ 
                                                                        '<textarea class="form_textarea preview" name="" id="" readonly="readonly" disabled="disabled" style="height: 100px"></textarea>'+ 
                                                                        '</td>'+ 
                                                                    '</tr>'+ 
                                                                    '<tr>'+ 
                                                                        '<th>업무별 우선순위</th>'+ 
                                                                        '<td colspan="5" class="in_button">'+ 
                                                                            '<textarea class="form_textarea preview" name="" id="" readonly="readonly" disabled="disabled" style="height: 100px"></textarea>'+ 
                                                                            '</td>'+ 
                                                                        '</tr>'+ 
                                            
                        '</tbody>'+ 
                '</table>'+ 
        '</div>';
        $('.view_box').append(paper_item);
    }
    
    });