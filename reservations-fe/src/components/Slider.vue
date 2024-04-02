<template>
  <section class="section-slider height-v">
        <div class="item">
          <img alt="Third slide" src="../assets/images/slider01.webp" class="img-responsive">
          <div class="carousel-caption">
            <h1>Welcome to Emerald Bay</h1>
            <p><span class="line-t"></span>Island Resort & Villas <span class="line-b"></span></p>
          </div>
        </div>

    <div class="check-avail">
      <div class="container">
        <div class="arrival date-title ">
          <label>Arrival Date </label>
          <div id="datepicker" class="input-group date" data-date-format="dd-mm-yyyy">
            <input class="form-control" type="text">
            <span class="input-group-addon"><img src="../assets/images/Home-1/date-icon.png" alt="#"></span>
          </div>
        </div>
        <div class="departure date-title ">
          <label>Departure Date </label>
          <div id="datepickeri" class="input-group date" data-date-format="dd-mm-yyyy">
            <input class="form-control" type="text">
            <span class="input-group-addon"><img src="../assets/images/Home-1/date-icon.png" alt="#"></span>
          </div>
        </div>
        <div class="adults date-title ">
          <label>Adults</label>
          <form>
            <div class=" carousel-search">
              <div class="btn-group">
                <a class="btn dropdown-toggle " data-toggle="dropdown" href="#">2</a>
                <ul class="dropdown-menu">
                  <li><a>1</a></li>
                  <li><a>2</a></li>
                  <li><a>3</a></li>
                  <li><a>4</a></li>
                </ul>
              </div>
            </div>
          </form>
        </div>
        <div class="children date-title ">
          <label>Children</label>
          <form>
            <div class=" carousel-search">
              <div class="btn-group">
                <a class="btn dropdown-toggle " data-toggle="dropdown" href="#">2</a>
                <ul class="dropdown-menu">
                  <li><a>1</a></li>
                  <li><a>2</a></li>
                  <li><a>3</a></li>
                  <li><a>4</a></li>
                </ul>
              </div>
            </div>
          </form>
        </div>
        <div class="find_btn date-title">
          <div class="text-find">
            Check
            <br>Availability
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>

export default {
  components: {

  }
}

</script>

<style scoped>

</style>