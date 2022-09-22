// $('#datatable').DataTable({
//     'autoWidth': false,
//     'serverSide': true,
//     'processing': true,
//     'responsive': true,
//     'ajax': {
//       'url': './shops/data',
//       'type': 'GET',
//     },
//     columnDefs: [
//       {targets: 0, data: 'id'},
//       {targets: 1, data: 'dealer__name'},
//       {targets: 2, data: 'name'},
//       {targets: 3, data: 'shopcode'},
//       {targets: 4, data: 'tel'},
//       {targets: 5, data: 'fax'},
//       {targets: 6, data: 'homepage'},
//       {targets: 7, data: 'memo'},
//       {targets: 8, data: 'kana'},
//     ]
//   });
  

$(document).ready(function () {

    // 選択中のレコードid
    let selected = [];

    // DataTables 設定
    // https://datatables.net/reference/index
    let table = $('#datatable').DataTable({

        // scrollX: true,
        // autoWidth: false,
        // Server-side processing:Ajaxモードの設定
        // https://datatables.net/examples/server_side/simple.html
        processing: true,
        serverSide: true,
        ajax: "./shops/data",
        // ajax: "{% url 'mycontact:ShopsJson' %}",

        // responsive: true,
        
        // dom: 検索フィールド等の各種ウィジェットの配置
        // https://datatables.net/reference/option/dom
        // dom: 'lfrtip',

        // lengthMenu: １ページに表示させる件数のリスト
        // https://datatables.net/reference/option/lengthMenu
        // lengthMenu: [[10, 20, 50, -1], [10, 20, 50, "全件"]],
        lengthMenu: [[5, 10, 50, 100], [5, 10, 50, 100]],
        lengthChange: true,

        // pageLength: pageLengthの初期値
        // https://datatables.net/reference/option/pageLength
        pageLength: 5,

        // language: 表示メッセージのローカライズ
        // https://datatables.net/reference/option/language
        // 日本語版ソース:https://github.com/DataTables/Plugins/blob/master/i18n/Japanese.lang
        language: {
            "thousands": ",",
            "sProcessing": "処理中...",
            "sLengthMenu": "_MENU_ 件",
            "sZeroRecords": "データはありません。",
            "sInfo": " _TOTAL_ 件中 _START_ ～ _END_ を表示",
            "sInfoEmpty": "データ無し",
            "sInfoFiltered": "（全 _MAX_ 件より抽出）",
            "sInfoPostFix": "",
            // "sSearch": "検索:",
            "sSearch": "店舗etc...",
            "sUrl": "",
            "oPaginate": {
                "sFirst": "<<",
                "sPrevious": "<",
                "sNext": ">",
                "sLast": ">>",
            },
        },
        // rowCallback: 行の描画時に追加処理を行いたいときに使う。
        // https://datatables.net/reference/option/rowCallback

        // ページ遷移時に選択済みの行の表示を変更している。
        rowCallback: function (row, data) {
            $(row).attr('data-id', data[0]);
            if ($.inArray(data[0], selected) !== -1) {
                $(row).addClass('selected');
            }
        },

        // columns: 列の設定
        // https://datatables.net/reference/option/columns

        // 列の設定は 'columns' または 'columnDefs' で行う。
        // columns のほうが冗長な記述になるが視認性が良い気がする。

        // BaseDatatableViewのcolumnsの設定順にフィールドが列に割り当てられる。
        // columnsのフィールド数より列数が少ないとエラーになるので注意。

        // columnsと実際の列表示の内容を変更したい場合は以下のオプションで工面するとよい。

        // visible: bool    列の表示/非表示
        // data: number     違う列のデータを表示
        // render: function 関数でデータを加工

        // render内で他の列のデータを使うこともできる。
        // https://datatables.net/manual/data/renderers

        // columnDefs: [
        //         {targets: 0, data: 'id'},
        //         {targets: 1, data: 'dealer__name'},
        //         {targets: 2, data: 'name'},
        //         {targets: 3, data: 'shopcode'},
        //         {targets: 4, data: 'tel'},
        //         {targets: 5, data: 'fax'},
        //         {targets: 6, data: 'homepage'},
        //         {targets: 7, data: 'memo'},
        //         {targets: 8, data: 'kana'},
        //       ],

        columns: [
            {
                // 1列目(id)
                title: "&nbsp;",
                // className: 'select-checkbox',
                searchable: false,
                visible: false,
                render: function () {
                    return "";
                },
            },
            {
                // 2列目
                title: "販社",
                // className: "all",
                // render: function (data, type, row) { //typeも必要
                //     // return '<a class="text-gray-800" data-toggle="modal" data-target="#exampleModal-'+ data + '">'+ data +'';
                //     return '<a class="" data-toggle="modal" data-target="#exampleModal" \
                //     data-sample="<b>' + row[12]+"</b><hr>・お客様相談室："+row[14]+"<hr>・緊急サポートダイヤル："+row[15]+"<hr>・ドメイン："+row[13]+"<hr>・NFS営業事務所："+row[19]+"　"+row[20]+"<hr>・コード："+row[10] +" ／ "+ row[11] +"<hr>・BC/本部："+row[16]+"<hr>・NFSメンテ："+row[17] +"　・自社メンテ："+row[18] + '">'+ data +'</a>';
                // },
                render: function (data, type, row) { //typeも必要
                    // return '<a class="text-gray-800" data-toggle="modal" data-target="#exampleModal-'+ data + '">'+ data +'';
                    var table1 = "<table class='table'><tr><td>お客様相談室</td><td>"+row[14]+"\
                                </td></tr><tr><td>緊急サポートダイヤル</td><td>"+row[15]+"\
                                </td></tr><tr><td>ドメイン</td><td>"+row[13]+"\
                                </td></tr><tr><td>NFS営業事務所</td><td>"+row[19]+"　"+row[20]+"\
                                </td></tr><tr><td>コード</td><td>"+row[10]+" ／ "+row[11]+"\
                                </td></tr><tr><td>BC/本部</td><td>"+row[16]+"\
                                </td></tr><tr><td>NFSメンテ</td><td>"+row[17]+"\
                                </td></tr><tr><td>自社メンテ</td><td>"+row[18]+"</td></tr></table>";
                    return row[10]+"　"+'<a class="" data-toggle="modal" data-target="#exampleModal" data-title="<b>' + row[12]+'</b>"\
                    data-sample="' + table1 + '">'+ data +'</a>';
                },

            },
            {
                // 3列目
                title: "店舗",
                // className: " all",
                // className: 'control',
                render: function (data, type, row) {
                    var targetStr = row[6]
                    if (targetStr.indexOf('http') != -1) {
                        return row[3]+"　"+'<a class="" target="_blank" href="' + row[6] + '">' + data + '</a>'+'　<span class="text-xs">（' +row[8]+'）</span>';
                    }else{
                        return row[3]+"　"+data + '</a>'+'　<span class="text-xs">（' +row[8]+'）</span>';
                    }
                },
            },
            {
                // 4列目
                title: "コード",
                visible: false,
                // className: " all",
            },
            {
                // 5列目
                title: "TEL",
            },
            {
                // 6列目
                title: "FAX",
                // visible: false,
            },
            {
                // 7列目
                title: "HP",
                visible: false,
            },
            {
                // 8列目
                title: "メモ",
                visible: false, // これでもサーチ対象のままになる
            },
            {
                // 9列目
                title: "店舗カナ",
                visible: false,
                // visible: false,
            },
            {
                title: "", //10pk
                visible: false,
            },
            {
                title: "",//11
                visible: false,
            },
            {
                title: "",//12
                visible: false,
            },
            {
                title: "",//13
                visible: false,
            },
            {
                title: "",//14
                visible: false,
            },
            {
                title: "",//15
                visible: false,
            },
            {
                title: "",//16
                visible: false,
            },
            {
                title: "",//17
                visible: false,
            },
        ],

        // 列の表示非表示ボタン
        // dom: 'Bfrtip',
        // buttons: [
        //     'colvis'
        // ],
        
    });

    //2つ目のテーブルテスト
    var oTable = $('#datatable2').dataTable({
        "processing": true,
        "serverSide": true,
        "ajax": "./shops/data2",

        lengthMenu: [[5, 10, 50, 100], [5, 10, 50, 100]],
        lengthChange: true,

        language: {
            "sLengthMenu": "_MENU_ 件（2022/7/2時点データ）",
            "sSearch": "CAコードetc...",
        },

        // columnDefs: [
        //             {targets: 0, data: 'Dealer'},
        //             {targets: 1, data: 'shop'},
        //             {targets: 2, data: 'cacode'},
        //             {targets: 3, data: 'name'},
        //             {targets: 4, data: 'kana'},
        //           ],

        columns: [
        {
            // 1列目(id)
            title: "&nbsp;",
            searchable: false,
            visible: false,
            render: function () {
                return "";
            },
        },
        {
            // 2列目
            title: "販社",
        },
        {
            // 3列目
            title: "店舗コード",
            // class: 'col-1',
            // render: function (data) {
            //     return data.replace("xxx", "");
            // },
            visible: false,
            render: function () {
                return "";
            },
        },
        {
            // 3列目
            title: "店舗",
            render: function (data, type, row) { //typeも必要
                return row[2].replace("xxx", "") +"　"+ data;
            },
        },
        {
            // 4列目
            title: "CAコード",
            render: function (data) {
                return data.replace("xxx", "");
            },
        },
        {
            // 5列目
            title: "CA",
        },
        {
            // 6列目
            title: "カナ",
        },
    ],
    });
    

});