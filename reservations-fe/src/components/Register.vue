<template>
  <div class="container-fluid">
    <div class="background-image"></div>
    <div class="row align-items-center justify-content-center">
      <div class="col col-12 col-sm-6 col-md-10 col-lg-6">
        <div v-if="showMsg === 'error'" class="alert alert-danger" role="alert">
          Invalid username or password or user already exists. Please Try again.
        </div>
        <div class="card">
          <div class="card-header">Register</div>
          <div class="card-body">
            <!-- Input Field Section -->
            <form ref="form">
              <div class="container-fuild">
                <div class="form-group row justify-content-left py-2">
                  <label class="col-4">Username</label>
                  <div class="col col-8">
                    <input name="username" v-model="credentials.username" type="text" required
                           class="form-control-sm form-control">
                  </div>
                </div>
                <div class="form-group row justify-content-end py-2">
                  <label class="col-4">Password</label>
                  <div class="col col-8">
                    <input v-model="credentials.password" type="password" class="form-control-
sm form-control">
                  </div>
                </div>
                <div class="form-group row justify-content-left py-2">
                  <label class="col-4">Re-enter password</label>
                  <div class="col col-8">
                    <input v-model="credentials.password2" type="password" class="form-control-
sm form-control">
                  </div>
                </div>
                <div class="form-group row justify-content-left py-2">
                  <label class="col-4">Email</label>
                  <div class="col col-8">
                    <input v-model="credentials.email" type="email" class="form-control-sm form-
control">
                  </div>
                </div>
                <div class="form-group row justify-content-left py-2">
                  <label class="col-4">First Name</label>
                  <div class="col col-8">
                    <input v-model="credentials.first_name" type="text" class="form-control-sm
form-control">
                  </div>
                </div>
                <div class="form-group row justify-content-left py-2">
                  <label class="col-4">Last Name</label>
                  <div class="col col-8">
                    <input v-model="credentials.last_name" type="text" class="form-control-sm
form-control">
                  </div>
                </div>
                <div class="row justify-content-around">
                  <div type="button" class="btn btn-secondary col-6" @click="login">Back to
                    Login
                  </div>
                  <div type="button" class="btn btn-primary col-4" @click="register">Register</div>
                </div>
              </div>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import router from '../router';
import {APIService} from '@/http/ApIService';

const apiService = new APIService();
export default {
  name: 'Register',
  data: () => ({
    credentials: {},
    password: "",
    repassword: "",
    valid: true,
    showMsg: '',
    showPassword: false,
  }),
  methods: {
    register() {
      apiService.registerUser(this.credentials)
          .then(response => {
            if (response.status === 201) {
              this.showMsg = "";
              router.push('/auth/');
            } else {
              this.showMsg = "error";
            }
          }).catch(error => {
        this.showMsg = "error";
        router.push("/register");
      });
    },
    login() {
      router.push('/auth/');
    }
  }
}
</script>

<style scoped>
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
  border: none;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
  overflow: hidden;
  width: 500px;
}

.card-header {
  background-color: #004445;
  color: #ffffff;
  padding: 16px 24px;
  font-size: 24px;
  font-weight: 300;
  text-align: center;
}

.alert-danger {
  margin: 16px 0;
  text-align: center;
  border-radius: 4px;
  padding: 15px;
  width: 500px;
}

.card-body {
  padding: 32px;
  background: #ffffff;
}

.form-group {
  margin-bottom: 15px;
}

label {
  color: #333;
  font-weight: 500;
}

.form-control-sm {
  border-radius: 4px;
  border: 1px solid #ccc;
  padding: 10px;
}

.btn-primary {
  padding: 7px 30px;
  border: #dcb324 1px solid;
  text-transform: uppercase;
  background-color: #d78f00;
  color: #1c212d;
  font-size: 14px;
  cursor: pointer;
  font-weight: 500;
  margin-left: 12px;
}

.btn-primary:hover {
  background-color: #1c212d;
  border: #d78f00 1px solid;
}

.btn-secondary {
  padding: 7px 30px;
  border: #004445 1px solid;
  text-transform: uppercase;
  background-color: #1c212d;
  color: white;
  font-size: 14px;
  cursor: pointer;
  font-weight: 500;
}

.btn-secondary:hover {
  background-color: #d78f00;
  border: #1c212d 1px solid;
}

.btn:active {
  transform: translateY(2px);
  color: inherit !important;
  background: inherit !important;
}
</style>
