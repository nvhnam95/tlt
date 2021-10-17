import axios from "axios";
import $ from "jquery";
import moment from "moment";
var tool_mixin =  {
    mounted(){
      $.fn.dataTable.Api.register( 'sum()', function ( ) {
        return this.flatten().reduce( function ( a, b ) {
            if ( typeof a === 'string' ) {
                a = a.replace(/[^\d.-]/g, '') * 1;
            }
            if ( typeof b === 'string' ) {
                b = b.replace(/[^\d.-]/g, '') * 1;
            }
     
            return a + b;
        }, 0 );
    } );
    },
    methods: {
        export_excel(additional_data=[]){
            let base_url = process.env.VUE_APP_API_ENDPOINT;
            let url = base_url + "/api/v1/tools/to-xlsx";
            let cell_raw_data = this.table.rows({filter:'applied'}).data()

            let table_header_text = []
            let table_header_name = []
            let table_data = []
      
            this.table.columns().every(function() {
              table_header_text.push( this.header().textContent )
            })
      
            for (let c=0; c < this.columns.length-1; c++){
              table_header_name.push(this.columns[c].data)
            }

            for (let d=0; d < cell_raw_data.length; d++){
              let row = []
              for (let c=0; c < table_header_name.length; c++){
                row.push(cell_raw_data[d][table_header_name[c]])
              }
              table_data.push(row)
            }
            if (additional_data.length) 
              table_data = [].concat(additional_data, [" "], [table_header_text], table_data)
            else table_data = [].concat([table_header_text], table_data)
            // Download file
            axios({
              url: url,
              method: 'post',
              data: table_data,
              responseType: 'blob',
            }).then((response) => {
              const url = window.URL.createObjectURL(new Blob([response.data]));
              const link = document.createElement('a');
              link.href = url;
              link.setAttribute('download', this.export_file_name + '.xlsx');
              document.body.appendChild(link);
              link.click();
            });
          },
          generate_search_boxes() {
            $("#poes_table tfoot th").each(function () {
              var title = $(this).text();
              $(this).html('<input type="text" placeholder="Tìm ' + title + '" />');
            });
      
            // Date range
            var start = moment();
            var end = moment();
            $("#date-filter-start").daterangepicker(
              {
                singleDatePicker: true,
                locale: {
                  format: "DD/MM/YYYY",
                  separator: " - ",
                  applyLabel: "OK",
                  cancelLabel: "Hủy",
                  fromLabel: "Từ",
                  toLabel: "Đến",
                  customRangeLabel: "Chọn khoảng thời gian",
                  weekLabel: "W",
                  daysOfWeek: ["CN", "T2", "T3", "T4", "T5", "T5", "T7"],
                  monthNames: [
                    "Tháng 1",
                    "Tháng 2",
                    "Tháng 3",
                    "Tháng 4",
                    "Tháng 5",
                    "Tháng 6",
                    "Tháng 7",
                    "Tháng 8",
                    "Tháng 9",
                    "Tháng 10",
                    "Tháng 11",
                    "Tháng 12",
                  ],
                  firstDay: 1,
                },
              },
              this.date_range_filter_callback_for_start
            );
      
            $("#date-filter-end").daterangepicker(
              {
                singleDatePicker: true,
                startDate: start,
                endDate: end,
                locale: {
                  format: "DD/MM/YYYY",
                  separator: " - ",
                  applyLabel: "OK",
                  cancelLabel: "Hủy",
                  fromLabel: "Từ",
                  toLabel: "Đến",
                  customRangeLabel: "Chọn khoảng thời gian",
                  weekLabel: "W",
                  daysOfWeek: ["CN", "T2", "T3", "T4", "T5", "T5", "T7"],
                  monthNames: [
                    "Tháng 1",
                    "Tháng 2",
                    "Tháng 3",
                    "Tháng 4",
                    "Tháng 5",
                    "Tháng 6",
                    "Tháng 7",
                    "Tháng 8",
                    "Tháng 9",
                    "Tháng 10",
                    "Tháng 11",
                    "Tháng 12",
                  ],
                  firstDay: 1,
                },
              },
              this.date_range_filter_callback_for_end
            );
            $('input[id="date-filter-start"]').val("")
            $('input[id="date-filter-end"]').val("")
          },
          date_range_filter_callback_for_start(start, end) {
            this.date_filter_start = start
            end
            this.refresh_table_data();
          },
          date_range_filter_callback_for_end(start, end) {
            end
            this.date_filter_end = start
      
            this.refresh_table_data();
          },
          refresh_table_data() {
            let start = this.date_filter_start
            let end = this.date_filter_end

            if (this.table) {
              if (start && end) {
                let url = new URL(this.table.ajax.url())
                url.searchParams.set("start", start.format("YYYY-MM-DD"))
                url.searchParams.set("end", end.format("YYYY-MM-DD"))
                this.table.ajax.url(
                  url.href
                );
              }
              this.table.ajax.reload();
            }
          },
    }
 }

 export default tool_mixin;
