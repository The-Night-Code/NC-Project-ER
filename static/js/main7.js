function my_Func_edit_VT_State_1(cell_id){
    var state = document.getElementById("table1_etat_vt"+cell_id)

    var url2="{% url 'VT_Page_edit_state' %}?"+
          "param0=" + cell_id +
          "&param1=" + state ;
        window.location.href = url2;
    
}