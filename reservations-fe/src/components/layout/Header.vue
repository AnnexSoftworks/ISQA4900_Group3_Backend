<template>
  <div v-click-outside="closeMobileNav">
    <header>
      <nav>
        <div class="branding">
          <Logo class="logo"></Logo>
        </div>
        <ul v-show="!mobile" class="navigation">
          <li>
            <router-link active-class="link-active" class="link" :to="{name: 'Home'}">Home</router-link>
          </li>
          <li>
            <router-link active-class="link-active" class="link" :to="{name: 'About'}">About</router-link>
          </li>
          <li class="position-relative">
            <a class="link" :class="{ 'link-active': isEntertainmentRoute }" @click="toggleEntertainment">
              Amenities
              <i class="fa fa-angle-down icon-entertainment" :class="{'icon-active' : entertainment}"></i>
            </a>
          </li>
          <li>
            <router-link active-class="link-active" class="link" :to="{name: 'Reservations'}">Reservations</router-link>
          </li>
          <li>
            <router-link active-class="link-active" class="link" :to="{name: 'Contact'}">Contact</router-link>
          </li>
          <li v-if="isWorker" class="position-relative">
            <a class="link" :class="{ 'link-active': isServiceRoute }" @click="toggleService">
              Other
              <i class="fa fa-angle-down icon-service" :class="{'icon-active' : service}"></i>
            </a>
          </li>
        </ul>
        <LoginButton v-if="!mobile && !isLoggedIn" class="login-button"></LoginButton>
        <svg v-else-if="!mobile && isLoggedIn" @click="toggleUserinfo" class="account-svg"
             :class="{ 'svg-active': isUserinfoRoute }" xmlns="http://www.w3.org/2000/svg" height="1em"
             viewBox="0 0 448 512">
          <!--! Font Awesome Free 6.4.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2023 Fonticons, Inc. -->
          <path
              d="M304 128a80 80 0 1 0 -160 0 80 80 0 1 0 160 0zM96 128a128 128 0 1 1 256 0A128 128 0 1 1 96 128zM49.3 464H398.7c-8.9-63.3-63.3-112-129-112H178.3c-65.7 0-120.1 48.7-129 112zM0 482.3C0 383.8 79.8 304 178.3 304h91.4C368.2 304 448 383.8 448 482.3c0 16.4-13.3 29.7-29.7 29.7H29.7C13.3 512 0 498.7 0 482.3z"/>
        </svg>
        <div class="icon">
          <i @click="toggleMobileNav" v-show="mobile" class="fa fa-bars" :class="{'icon-active' : mobileNav}"></i>
        </div>
      </nav>

      <transition name="mobile-nav">
        <div v-show="mobileNav" class="dropdown-nav">
          <div class="scrollable-list">
            <div class="branding-mobile">
              <Logo class="logo"></Logo>
            </div>
            <ul>
              <li>
                <router-link active-class="link-active" class="link" :to="{name: 'Home'}" @click="toggleMobileNav">
                  Home
                </router-link>
              </li>
              <li>
                <router-link active-class="link-active" class="link" :to="{name: 'About'}" @click="toggleMobileNav">
                  About
                </router-link>
              </li>
              <li class="position-relative">
                <a class="link" :class="{ 'link-active': isEntertainmentRoute }" @click="toggleEntertainment">
                  Amenities
                  <i class="fa fa-angle-down icon-entertainment" :class="{'icon-active' : entertainment}"></i>
                </a>
              </li>

              <transition name="submenu-mobile">
                <ul v-if="entertainment">
                  <li>
                    <router-link active-class="link-active" class="sub-link" :to="{name: ''}" @click="toggleMobileNav">
                      Ocean Spa & Wellness Center
                    </router-link>
                  </li>
                  <li>
                    <router-link active-class="link-active" class="sub-link" :to="{name: ''}" @click="toggleMobileNav">
                      Gourmet Dining
                    </router-link>
                  </li>
                  <li>
                    <router-link active-class="link-active" class="sub-link" :to="{name: ''}" @click="toggleMobileNav">
                      Exclusive Marina Services
                    </router-link>
                  </li>
                  <li>
                    <router-link active-class="link-active" class="sub-link" :to="{name: ''}" @click="toggleMobileNav">
                      Island Golf Retreat
                    </router-link>
                  </li>
                  <li>
                    <router-link active-class="link-active" class="sub-link" :to="{name: ''}" @click="toggleMobileNav">
                      Fitness Pavilion
                    </router-link>
                  </li>
                  <li>
                    <router-link active-class="link-active" class="sub-link" :to="{name: ''}" @click="toggleMobileNav">
                      Kid's Paradise Club
                    </router-link>
                  </li>
                </ul>
              </transition>

              <li>
                <router-link active-class="link-active" class="link" :to="{name: 'Reservations'}"
                             @click="toggleMobileNav">Reservations
                </router-link>
              </li>
              <li>
                <router-link active-class="link-active" class="link" :to="{name: 'Contact'}"
                             @click="toggleMobileNav">Contact
                </router-link>
              </li>
              <li v-if="isWorker" class="position-relative">
                <a class="link" :class="{ 'link-active': isServiceRoute }" @click="toggleService">
                  Services
                  <i class="fa fa-angle-down icon-service-mobile" :class="{'icon-active' : service}"></i>
                </a>
              </li>

              <transition name="submenu-mobile">
                <ul v-if="service">
                  <li v-if="isAdmin">
                    <router-link active-class="link-active" class="sub-link" :to="{name: 'ServiceRooms'}"
                                 @click="toggleMobileNav">Rooms
                    </router-link>
                  </li>
                  <li v-if="isAdmin">
                    <router-link active-class="link-active" class="sub-link" :to="{name: 'ServiceEntertainment'}"
                                 @click="toggleMobileNav">Entertainment
                    </router-link>
                  </li>
                  <li v-if="isAdmin || isHousekeepingWorker">
                    <router-link active-class="link-active" class="sub-link" :to="{name: 'ServiceHousekeeping'}"
                                 @click="toggleMobileNav">Housekeeping
                    </router-link>
                  </li>
                  <li v-if="isAdmin || isRestaurantWorker">
                    <router-link active-class="link-active" class="sub-link" :to="{name: 'ServiceRestaurant'}"
                                 @click="toggleMobileNav">Restaurant
                    </router-link>
                  </li>
                  <li v-if="isAdmin">
                    <router-link active-class="link-active" class="sub-link" :to="{name: 'ServiceAccounts'}"
                                 @click="toggleMobileNav">Accounts
                    </router-link>
                  </li>
                  <li v-if="isAdmin">
                    <router-link active-class="link-active" class="sub-link" :to="{name: 'ServicePrices'}"
                                 @click="toggleMobileNav">Prices
                    </router-link>
                  </li>
                </ul>
              </transition>

              <LoginButton v-if="!isLoggedIn" class="login-button-mobile"></LoginButton>
              <li v-else-if="isLoggedIn">
                <svg @click="toggleUserinfo" class="account-svg-mobile" :class="{ 'svg-active': isUserinfoRoute }"
                     xmlns="http://www.w3.org/2000/svg" height="1em" viewBox="0 0 448 512">&lt;!&ndash;! Font Awesome
                  Free 6.4.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license
                  (Commercial License) Copyright 2023 Fonticons, Inc. &ndash;&gt;<path
                      d="M304 128a80 80 0 1 0 -160 0 80 80 0 1 0 160 0zM96 128a128 128 0 1 1 256 0A128 128 0 1 1 96 128zM49.3 464H398.7c-8.9-63.3-63.3-112-129-112H178.3c-65.7 0-120.1 48.7-129 112zM0 482.3C0 383.8 79.8 304 178.3 304h91.4C368.2 304 448 383.8 448 482.3c0 16.4-13.3 29.7-29.7 29.7H29.7C13.3 512 0 498.7 0 482.3z"/>
                </svg>
              </li>

              <transition name="submenu-mobile">
                <ul v-if="userinfo">
                  <li>
                    <router-link active-class="link-active" class="sub-link" :to="{name: 'MyAccount'}"
                                 @click="toggleMobileNav">My account
                    </router-link>
                  </li>
                  <li>
                    <router-link active-class="link-active" class="sub-link" :to="{name: 'MyBookings'}"
                                 @click="toggleMobileNav">My Bookings
                    </router-link>
                  </li>
                  <li>
                    <router-link active-class="link-active" class="sub-link" :to="{name: 'MyRooms'}"
                                 @click="toggleMobileNav">Rooms
                    </router-link>
                  </li>
                  <li><p class="sub-link" @click="logout">Log out</p></li>
                </ul>
              </transition>
            </ul>
          </div>
        </div>
      </transition>
    </header>
    <transition name="submenu-nav">
      <div v-if="!mobile && entertainment" class="submenu-navigation">
        <ul class="navigation">
          <li>
            <router-link active-class="link-active" class="link" :to="{name: ''}">Ocean Spa & Wellness Center
            </router-link>
          </li>
          <li>
            <router-link active-class="link-active" class="link" :to="{name: ''}">Gourmet Dining</router-link>
          </li>
          <li>
            <router-link active-class="link-active" class="link" :to="{name: ''}">Exclusive Marina Services
            </router-link>
          </li>
          <li>
            <router-link active-class="link-active" class="link" :to="{name: ''}">Island Golf Retreat</router-link>
          </li>
          <li>
            <router-link active-class="link-active" class="link" :to="{name: ''}">Fitness Pavilion</router-link>
          </li>
          <li>
            <router-link active-class="link-active" class="link" :to="{name: ''}">Kid's Paradise Club</router-link>
          </li>
        </ul>
      </div>
    </transition>

    <transition name="submenu-nav">
      <div v-if="!mobile && userinfo" class="submenu-navigation">
        <ul class="navigation">
          <li>
            <router-link active-class="link-active" class="link" :to="{name: 'MyAccount'}">My account</router-link>
          </li>
          <li>
            <router-link active-class="link-active" class="link" :to="{name: 'MyBookings'}">My Bookings</router-link>
          </li>
          <li>
            <router-link active-class="link-active" class="link" :to="{name: 'MyRooms'}">Rooms</router-link>
          </li>
          <li><p class="link" @click="logout">Log out</p></li>
        </ul>
      </div>
    </transition>

    <transition name="submenu-nav">
      <div v-if="!mobile && service" class="submenu-navigation">
        <ul class="navigation">
          <li v-if="isAdmin">
            <router-link active-class="link-active" class="link" :to="{name: 'ServiceRooms'}">Rooms</router-link>
          </li>
          <li v-if="isAdmin">
            <router-link active-class="link-active" class="link" :to="{name: 'ServiceEntertainment'}">Entertainment
            </router-link>
          </li>
          <li v-if="isAdmin || isHousekeepingWorker">
            <router-link active-class="link-active" class="link" :to="{name: 'ServiceHousekeeping'}">Housekeeping
            </router-link>
          </li>
          <li v-if="isAdmin || isRestaurantWorker">
            <router-link active-class="link-active" class="link" :to="{name: 'ServiceRestaurant'}">Restaurant
            </router-link>
          </li>
          <li v-if="isAdmin">
            <router-link active-class="link-active" class="link" :to="{name: 'ServiceAccounts'}">Accounts</router-link>
          </li>
          <li v-if="isAdmin">
            <router-link active-class="link-active" class="link" :to="{name: 'ServicePrices'}">Prices</router-link>
          </li>
        </ul>
      </div>
    </transition>

  </div>
</template>

<script>
import Logo from "@/components/layout/Logo.vue";
import LoginButton from "@/components/layout/LoginButton.vue";
import vClickOutside from "click-outside-vue3";

export default {
  components: {
    Logo,
    LoginButton
  },

  data() {
    return {
      mobile: null,
      mobileNav: null,
      windowWidth: null,
      entertainment: false,
      service: false,
      userinfo: false
    };
  },
  created() {
    window.addEventListener("resize", this.checkScreen);
    this.checkScreen();
  },
  methods: {
    toggleMobileNav() {
      this.closeEntertainment();
      this.closeUserinfo();
      this.closeService();
      this.mobileNav = !this.mobileNav;
    },
    closeMobileNav() {
      this.closeEntertainment();
      this.closeUserinfo();
      this.closeService();
      this.mobileNav = false;
    },
    toggleEntertainment() {
      this.closeUserinfo();
      this.closeService();
      this.entertainment = !this.entertainment;
    },
    toggleService() {
      this.closeEntertainment();
      this.closeUserinfo();
      this.service = !this.service;
    },
    closeService() {
      this.service = false;
    },
    closeEntertainment() {
      this.entertainment = false;
    },
    toggleUserinfo() {
      this.closeEntertainment();
      this.closeService();
      this.userinfo = !this.userinfo;
    },
    closeUserinfo() {
      this.userinfo = false;
    },
    closeAll() {
      this.closeEntertainment();
      this.closeUserinfo();
      this.closeService();
    },
    checkScreen() {
      this.windowWidth = window.innerWidth;
      if (this.windowWidth <= 1200) {
        this.mobile = true;
      } else {
        this.mobile = false;
        this.mobileNav = false;
      }
    },
    logout() {
      this.closeAll();
      this.$store.dispatch('auth/logout').then(() => {
        this.$router.push({name: "Home"}).then(() => window.location.reload());
      });
    },
  },
  computed: {
    isLoggedIn() {
      return this.$store.getters['auth/isAuthenticated'];
    },
    isEntertainmentRoute() {
      const route = this.$route.name;
      return route === '' || route === '' || route === '' || route === '' || route === '' || route === '';
    },
    isServiceRoute() {
      const route = this.$route.name;
      return route === 'ServicePrices' || route === 'ServiceAccounts' || route === 'ServiceRestaurant' || route === 'ServiceHousekeeping' || route === 'ServiceEntertainment' || route === 'ServiceRooms';
    },
    isUserinfoRoute() {
      const route = this.$route.name;
      return route === 'MyAccount' || route === 'MyBookings' || route === 'MyRooms';
    },
    isWorker() {
      return this.isRestaurantWorker || this.isHousekeepingWorker || this.isAdmin;
    },
    isRestaurantWorker() {
      return this.$store.getters['auth/isRestaurant'];
    },
    isHousekeepingWorker() {
      return this.$store.getters['auth/isCleaner'];
    },
    isAdmin() {
      return this.$store.getters['auth/isAdmin'];
    }
  },
  directives: {
    clickOutside: vClickOutside.directive
  },
}
</script>

<style scoped>

.position-relative {
  position: relative;
}

.icon-entertainment {
  position: absolute;
  top: 17px;
  left: 118px;
}

.icon-service {
  position: absolute;
  top: 17px;
  left: 73px;
}

.icon-service-mobile {
  position: absolute;
  top: 17px;
  left: 95px;
}

header {
  background-color: #1F232C;
  z-index: 1000;
  width: 100%;
  transition: 0.5s ease all;
  color: white;
  position: relative;
}

nav {
  position: relative;
  display: flex;
  flex-direction: row;
  align-items: center;
  padding: 7px 0;
  transition: 0.5s ease all;
  width: 97%;
  margin: 0 auto;
}

ul,
.link {
  text-align: center;
  list-style: inside;
  color: white;
  text-decoration: none;
  list-style: none;
}

li {
  padding: 16px;
  margin-left: 16px;
}

.link {
  font-size: 15px;
  padding-bottom: 4px;
  border-bottom: 1px solid transparent;
}

.link:hover {
  color: #d78f00;
  cursor: pointer;
}

ul,
.sub-link {
  color: rgba(255, 255, 255, 0.77);
  text-decoration: none;
  list-style: none;
  cursor: pointer;
}

.sub-link {
  font-size: 13px;
  transition: 0.2s ease all;
  padding-bottom: 4px;
  border-bottom: 1px solid transparent;
}

.sub-link:hover {
  color: #d78f00;
}

.link-active {
  color: #d78f00;
}

.branding {
  display: flex;
  align-items: center;
}

.branding-mobile {
  padding-top: 20px;
  padding-bottom: 20px;
}

.logo {
  transition: 0.5s ease all;
  margin-left: 16px;
}

.navigation {
  display: flex;
  align-items: center;
  flex: 1;
  justify-content: center;
  gap: 25px;
  padding: 0;
  margin-top: 12px;
}

.login-button {
  display: flex;
  align-items: center;
  justify-content: flex-end;
}

.login-button-mobile {
  margin-top: 30px;
}

.account-svg {
  display: flex;
  align-items: center;
  fill: white;
  cursor: pointer;
  height: 1.2em;
  margin-right: 10px;
}

.account-svg:hover {
  fill: #d78f00;
}


.account-svg-mobile {
  fill: white;
  cursor: pointer;
  margin-top: 20px;
  height: 1.3em;
}

.account-svg-mobile:hover {
  fill: #d78f00;
}

.svg-active {
  fill: #d78f00;
}

.icon {
  display: flex;
  align-items: center;
  position: absolute;
  top: 0;
  right: 24px;
  height: 100%;
}

.icon:hover {
  color: #d78f00;
}

i {
  cursor: pointer;
  font-size: 20px;
  transition: transform 0.4s ease;
}

.icon-active {
  transform: rotate(180deg);
}

.dropdown-nav {
  display: flex;
  flex-direction: column;
  position: fixed;
  width: 100%;
  max-width: 250px;
  height: 100%;
  max-height: 100vh; /* limit the height to the viewport's height */
  background-color: #1F232C;
  top: 0;
  left: 0;
  align-items: center; /* center items again */
  justify-content: center;
  padding-bottom: 16px; /* provide some space at the bottom */
}

.dropdown-nav li {
  background-color: #1F232C;
}

.scrollable-list {
  max-height: calc(100vh - 50px); /* adjust this based on your logo and button height */
  overflow-y: auto; /* allow scrolling */
  width: 100%; /* take full width of parent */
  display: flex;
  flex-direction: column;
  align-items: center; /* center items */
  text-decoration: none;
  list-style: none;
}

.dropdown-nav li {
  margin-left: 0;
}

.submenu-navigation {
  position: absolute;
  top: 60px;
  width: 100%;
  background-color: #1F232C;
  font-size: 13px;
  z-index: 900;
  box-shadow: 0 0 10px 0 rgba(0, 0, 0, 0.75);
}

.submenu-mobile-enter-from,
.submenu-mobile-leave-to {
  max-height: 0;
  opacity: 0;

}

.submenu-mobile-enter-active {
  transition: all 0.25s ease-in-out;
}

.submenu-mobile-leave-active {
  transition: all 0.25s ease-in-out;
}

.submenu-mobile-enter-to,
.submenu-mobile-leave-from {
  max-height: 400px;
  opacity: 1;

}

.submenu-nav-enter-from,
.submenu-nav-leave-to {
  transform: translateY(-100%);
}

.submenu-nav-enter-active {
  transition: transform 0.2s ease-in-out;
}

.submenu-nav-leave-active {
  transition: transform 0.2s ease-in-out;
}

.submenu-nav-enter-to,
.submenu-nav-leave-from {
  transform: translateY(0);
}

.mobile-nav-enter-active,
.mobile-nav-leave-active {
  transition: 0.3s ease all;
}

.mobile-nav-enter-from,
.mobile-nav-leave-to {
  transform: translateX(-250px);
}

.mobile-nav-enter-to {
  transform: translateX(0);
}

@media (max-width: 1200px) {
  nav {
    max-width: 1200px;
  }
}
</style>