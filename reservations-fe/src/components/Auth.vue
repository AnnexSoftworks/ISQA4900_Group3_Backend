<template>
  <div class="container-fluid">
    <div class="background-image"></div>
    <div class="row align-items-center justify-content-center">
      <div class="col-12 col-sm-6 col-md-4 col-lg-4">
        <div class="card mx-auto shadow">
          <div class="card-body">
            <div class="sky-h3"><span>ACCOUNT LOGIN</span></div>
            <div
                v-if="showMsg === 'loginError'"
                close-icon="mdi-close-circle"
                :value="true"
                class="alert alert-danger"
                role="alert"
                dense
            >
              Invalid username or password. Please Try again.
            </div>
            <div
                v-else-if="showMsg === 'axiosError'"
                close-icon="mdi-close-circle"
                :value="true"
                class="alert alert-danger"
                role="alert"
                dense
            >
              Access blocked by server. Check server.
            </div>
            <div class="card-text pt-2">
              <div class="col-md-10 mb-3">
                <div class="input-group">
                  <div class="input-group-prepend">
                  </div>
                  <input
                      v-model="credentials.username"
                      :counter="70"
                      label="Username"
                      :rules="rules.username"
                      maxlength="70"
                      required
                      type="text"
                      class="form-control mb-3"
                      style="margin-bottom: 20px;"
                      placeholder="Username"
                      aria-describedby="inputGroupPrepend2"
                  />
                  <div class="w-100"></div>
                  <div class="input-group-prepend">
                  </div>
                  <input
                      :type="showPassword ? 'text' : 'Password'"
                      v-model="credentials.password"
                      label="Password"
                      :rules="rules.password"
                      maxlength="20"
                      required
                      :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
                      @click:append="showPassword = ! showPassword"
                      class="form-control"
                      placeholder="Password"
                      aria-describedby="inputGroupPrepend2"
                  />
                </div>
              </div>
              <button ref="form" @click.prevent="login" class="btn btn-primary">Login</button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import router from '../router';
import {APIService} from "@/http/ApIService";

const apiService = new APIService();
export default {
  name: "Auth",
  data: () => ({
    credentials: {},
    valid: true,
    showMsg: "",
    loading: false,
    rules: {
      username: [
        (v) => !!v || "Username is required",
        (v) =>
            (v && v.length > 3) ||
            "A username must be more than 3 characters long",
        (v) =>
            /^[a-z0-9_]+$/.test(v) ||
            "A username can only contain letters and digits",
      ],
      password: [
        (v) => !!v || "Password is required",
        (v) =>
            (v && v.length > 7) ||
            "The password must be longer than 7 characters",
      ],
    },
    showPassword: false,
  }),
  methods: {
    login() {
      localStorage.clear();
      localStorage.setItem("isAuthenticated", false)
      apiService
          .authenticateLogin(this.credentials)
          .then((response) => {
            const access = response.data.access
            const refresh = response.data.refresh
            localStorage.setItem("access", access)
            localStorage.setItem("refresh", refresh)
            localStorage.setItem("isAuthenticated", true)
            localStorage.setItem("log_user", JSON.stringify(this.credentials.username))
            window.location = "/";
          }).catch(error => {
        if (error.message === "Network Error") { // Verify CORS middleware installed in server settings
          this.showMsg = "axiosError"
        } else if (error.response.status === 401) { // "not authorized"
          this.showMsg = "loginError";
          router.push("/auth");
        } else if (error.response.status === 400) { //"bad request"
          this.showMsg = "loginError";
        } else {
          this.showMsg = "axiosError";
          router.push("/auth");
        }
      });
    }
  }
}
</script>

<style scoped>

@import url('https://fonts.googleapis.com/css?family=Playfair+Display:400,700,900');
@import url('https://fonts.googleapis.com/css?family=Poppins:300,400,500,600,700,800');
@import url('https://fonts.googleapis.com/css?family=Montserrat:100,200,300,400,500,600,700,800,900');

.sky-h3 {
  font-family: "Poppins", sans-serif;
  text-shadow: 1px 1px 4px #000000;
  font-weight: 700;
}

.container-fluid {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  position: relative;
  overflow: hidden;
}

.background-image {
  content: '';
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  /* Keep the background image here */
  background: url('../assets/images/img01-blur.png') center center / cover no-repeat fixed;
  /* Adjust the blur value to your preference */
  backdrop-filter: blur(250px); /* Apply the blur effect here */
  -webkit-backdrop-filter: blur(250px); /* For Safari compatibility */
  z-index: -1; /* Place the pseudo-element behind the content */
}

.card {
  color: white;
  width: 600px;
  padding: 1.5rem;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.card-title span {
  font-size: 2rem; /* Adjust font size as needed */
  font-weight: bold;
}

.input-group {
  width: 362px;
  margin-bottom: 1rem;
}

.input-group-text {
  background: transparent;
  border: none;
  color: white;
}

.form-control {
  background: rgba(255, 255, 255, 0.1);
  border: 2px solid white; /* Gold border */
  border-radius: 0; /* Square edges */
  color: white;
  padding: 20px;
  width: 430px;
}

.form-control::placeholder {
  color: #ffffff;
  text-shadow: 1px 1px 1px #000000;
}

.btn-primary {
  padding: 7px 30px;
    background: rgba(255, 255, 255, 0.1);
  border: 2px solid white; /* Gold border */
  text-transform: uppercase;
  font-size: 14px;
  cursor: pointer;
  font-weight: 500;
  margin-left: 12px;
  border-radius: 0!important;
}

.btn-primary:hover {
  background-color: #1c212d;
  border: #d78f00 1px solid;
}

.btn:active {
  transform: translateY(2px);
  color: inherit !important;
  background: inherit !important;
}

.alert.alert-danger {
  font-size: 0.9rem;
  width: 100%; /* Full width */
  text-align: center;
  background: #c0392b; /* Red background for alert */
  margin-bottom: 1rem; /* Space between alert and title */
  border-radius: 4px; /* Rounded edges for alert */
}

/* Hide scrollbar for aesthetic purposes, but it can be kept if needed */
::-webkit-scrollbar {
  display: none;
}

/* Responsive adjustments */
@media (max-width: 576px) {
  .card {
    padding: 1rem;
    margin: 1rem;
  }

  .card-title span {
    font-size: 1.5rem;
  }
}

</style>
