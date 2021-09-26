<template>
<div>
  Home 
  VUE_APP_API_ENDPOINT: {{VUE_APP_API_ENDPOINT}}
</div>
</template>

<script>
export default {
  data: function () {
    return {
       "VUE_APP_API_ENDPOINT": process.env.VUE_APP_API_ENDPOINT
    }
  }
}

</script>