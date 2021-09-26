import axios from "axios";

var tool_mixin =  {
    methods: {
        export_excel(){
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
      
            table_data = [].concat([table_header_text], table_data)
      
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
    }
 }

 export default tool_mixin;
