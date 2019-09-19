<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
  @import url('https://fonts.googleapis.com/css?family=Karla');
</style>

<!-- firebase -->
<!--<template>-->
  <!--<div id="app">-->
    <!--<p v-if="loading"> Loading... </p>-->
    <!--<router-view v-else />-->
  <!--</div>-->
<!--</template>-->

<!--<script>-->
<!--import firebase from 'firebase'-->
<!--export default {-->
  <!--name: 'App',-->
  <!--data () {-->
    <!--return {-->
      <!--loading: true-->
    <!--}-->
  <!--},-->
  <!--methods: {-->
    <!--loginRedirect () {-->
      <!--return new Promise((resolve, reject) => {-->
        <!--window.location.href = '/Login'-->
        <!--resolve()-->
      <!--})-->
    <!--}-->
  <!--},-->
  <!--created () {-->
    <!--firebase.auth().onAuthStateChanged((user) => {-->
      <!--if (user) {-->
        <!--user.getIdToken().then((token) => {-->
          <!--this.initStore(token)-->
            <!--.then(() => { this.loading = false })-->
            <!--.catch(() => {-->
              <!--firebase.auth().signOut()-->
                <!--.then(() => {-->
                  <!--this.loginRedirect()-->
                    <!--.then(() => {-->
                      <!--this.loading = false-->
                    <!--})-->
                <!--})-->
            <!--})-->
        <!--})-->
      <!--} else { this.loading = false }-->
    <!--})-->
  <!--}-->
<!--}-->
<!--</script>-->

<!--<style>-->
  <!--@import url('https://fonts.googleapis.com/css?family=Karla');-->
<!--</style>-->
