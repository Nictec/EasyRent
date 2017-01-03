<template> 
    <button v-on:click="msg += 1">{{msg}}</button> 
</template> 
 


<script>
export default {
  data () {
    return {
      msg: 0
    }
  }
}
</script>