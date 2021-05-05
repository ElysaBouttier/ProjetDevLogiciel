<template>
  <div id="app">
    <v-app class="vapp">
      <v-app-bar app class="header" dense>
        <v-app-bar-nav-icon color="white"></v-app-bar-nav-icon>

        <v-toolbar-title>Manage app</v-toolbar-title>
        <v-spacer></v-spacer>

      </v-app-bar>

      <!-- Sizes your content based upon application components -->
      <v-main class="vmain">
        <!-- Provides the application the proper gutter -->
        <v-container fluid class="pa-0">
          <router-view></router-view>
        </v-container>
      </v-main>

        <v-btn>
          <router-link to="/about">About</router-link>
        </v-btn>

        <v-btn>
          <router-link to="/home">Home</router-link>
        </v-btn>

        <v-btn>
          <router-link to="/test">Test</router-link>
        </v-btn>
    </v-app>
  </div>
</template>


<script>
export default {
  name: "app",
  props: {},

  //   components: {},
  data: () => ({

  }),
  computed: {
  },
  methods: {
    
  },
};
</script>

<style lang="scss">
@import url('https://fonts.googleapis.com/css2?family=Nunito:wght@200&display=swap');

#app {
  .header {
    background-color: darkblue;
    color: white;
    .v-toolbar__title{
      font-family: 'Nunito', sans-serif;
    }
  }

  .bottomNavigation {
    background-color: darkblue;

    a{
    color: white;

    }
  }
  .bottomNavigation {
    a {
      text-decoration: none;
    }
  }
}
</style>
