<template>
  <section class="banner-tems text-center">
    <div class="container">
      <div class="banner-content">
        <h2 style="text-shadow: 1px 1px 4px #000000; margin-top: -88px;">Reservations</h2>
        <p style="text-shadow: 1px 1px 3px #000000;">Start Planning Your Dream Island Getaway</p>
      </div>
    </div>
  </section>

  <section class="section-reservation-page" style="margin: 44px 0 200px 0;">
    <div class="container">
      <div class="reservation-page">
        <div class="reservation_step">
          <ul>
            <li class="active"><a href="#"><span>1.</span> Choose Date</a></li>
            <li><a href="#"><span>2.</span> Choose Room</a></li>
            <li><a href="#"><span>3.</span> Make a Reservation</a></li>
            <li><a href="#"><span>4.</span> Confirmation</a></li>
          </ul>
        </div>

        <div class="row">
          <div class="col-lg-3 col-md-4 col-sm-12 col-xs-12">
            <div class="sidebar">
              <div class="widget widget_check_availability">
                <h4 class="widget-title">YOUR RESERVATION</h4>
                <div class="check_availability">
                  <h6 class="check_availability_title">reservation details</h6>
                  <div class="check_availability-field">
                    <label>Arrival Date</label>
                    <div class="input-group date" data-date-format="dd-mm-yyyy" id="datepicker1">
                      <input class="form-control wrap-box" type="text" placeholder="mm/dd/yyyy">
                      <span class="input-group-addon"><i class="fa fa-calendar" aria-hidden="true"></i></span>
                    </div>
                  </div>
                  <div class="check_availability-field">
                    <label>Nights</label>
                    <select class="awe-select">
                      <option>1</option>
                      <option>2</option>
                      <option>3</option>
                      <option>4</option>
                    </select>
                  </div>
                  <div class="check_availability-field">
                    <label>Departure Date</label>
                    <div id="datepicker2" class="input-group date" data-date-format="dd-mm-yyyy">
                      <input class="form-control wrap-box" type="text" placeholder="mm/dd/yyyy">
                      <span class="input-group-addon"><i class="fa fa-calendar" aria-hidden="true"></i></span>
                    </div>
                  </div>
                  <h6 class="check_availability_title">GUESTS</h6>

                  <div class="check_availability-field_group">
                    <div class="check_availability-field" style="margin: 18px 0 0 16px;">
                      <label># of Guests</label>
                      <select class="awe-select">
                        <option>1</option>
                        <option>2</option>
                        <option>3</option>
                        <option>4</option>
                        <option>5</option>
                        <option>6</option>
                      </select>
                    </div>


                  </div>

                  <button class="btn-room btn">CHECK AVAILABILITY</button>
                </div>
              </div>
              <!-- END / WIDGET CHECK AVAILABILITY -->
            </div>
          </div>
          <div class=" col-lg-9 col-md-8 col-sm-12 col-xs-12">
            <div class="reservation_content bg-gray">
              <h2 class="reservation-heading">Availability</h2>
              <div class="col-sm-6">
                <div class="reservation-calendar_custom">
                  <div class="reservation-calendar_title">
                    <span class="reservation-calendar_month">APRIL</span>
                    <span class="reservation-calendar_year"> 2024</span>
                    <a href="#" class="reservation-calendar_prev reservation-calendar_corner"><i
                        class="ion-ios-arrow-thin-left"></i></a>
                  </div>
                  <table class="reservation-calendar_tabel">
                    <thead>
                    <tr>
                      <th>Su</th>
                      <th>Mo</th>
                      <th>Tu</th>
                      <th>We</th>
                      <th>Th</th>
                      <th>Fr</th>
                      <th>Sa</th>
                    </tr>
                    </thead>
                    <tr>
                      <td></td>
                      <td class="reservation-calendar_current-date">
                        <a href="#"><small>1</small> <span>Today</span></a>
                      </td>
                      <td><a href="#"><small>2</small> </a></td>
                      <td class=" active"><a href="#"><small>3</small><span>Arrive</span></a></td>
                      <td class=" active"><a href="#"><small>4</small></a></td>
                      <td class=" active"><a href="#"><small>5</small></a></td>
                      <td class=" active"><a href="#"><small>6</small><span>Depart</span></a></td>
                    </tr>
                    <tr>
                      <td><a href="#"><small>7</small></a></td>
                      <td><a href="#"><small>8</small></a></td>
                      <td><a href="#"><small>9</small></a></td>
                      <td><a href="#"><small>10</small></a></td>
                      <td class="reservation-calendar_current-select"><a href="#"><small>11</small></a></td>
                      <td class="reservation-calendar_current-select"><a href="#"><small>12</small></a></td>
                      <td><a href="#"><small>13</small></a></td>
                    </tr>
                    <tr>
                      <td><a href="#"><small>14</small></a></td>
                      <td><a href="#"><small>15</small></a></td>
                      <td><a href="#"><small>16</small></a></td>
                      <td><a href="#"><small>17</small></a></td>
                      <td><a href="#"><small>18</small></a></td>
                      <td><a href="#"><small>19</small></a></td>
                      <td><a href="#"><small>20</small></a></td>
                    </tr>
                    <tr>
                      <td><a href="#"><small>21</small></a></td>
                      <td><a href="#"><small>22</small></a></td>
                      <td><a href="#"><small>23</small></a></td>
                      <td><a href="#"><small>24</small></a></td>
                      <td><a href="#"><small>25</small></a></td>
                      <td><a href="#"><small>26</small></a></td>
                      <td><a href="#"><small>27</small></a></td>
                    </tr>
                    <tr>
                      <td><a href="#"><small>28</small></a></td>
                      <td><a href="#"><small>29</small></a></td>
                      <td><a href="#"><small>30</small></a></td>
                      <td><a href="#"><small>31</small></a></td>
                      <td></td>
                      <td></td>
                      <td></td>
                    </tr>
                  </table>
                </div>
              </div>
              <div class="col-sm-6">
                <div class="reservation-calendar_custom">
                  <div class="reservation-calendar_title">
                    <span class="reservation-calendar_month">MAY</span>
                    <span class="reservation-calendar_year"> 2024</span>

                    <a href="#" class="reservation-calendar_next reservation-calendar_corner"><i
                        class="ion-ios-arrow-thin-right"></i></a>
                  </div>
                  <table class="reservation-calendar_tabel">
                    <thead>
                    <tr>
                      <th>Su</th>
                      <th>Mo</th>
                      <th>Tu</th>
                      <th>We</th>
                      <th>Th</th>
                      <th>Fr</th>
                      <th>Sa</th>
                    </tr>
                    </thead>
                    <tr>
                      <td></td>
                      <td class="reservation-calendar_current-date">
                        <a href="#"><small>1</small></a>
                      </td>
                      <td class="current-select"><a href="#"><small>2</small></a></td>
                      <td class="current-select"><a href="#"><small>3</small></a></td>
                      <td class="current-select"><a href="#"><small>4</small></a></td>
                      <td class="current-select"><a href="#"><small>5</small></a></td>
                      <td><a href="#"><small>6</small></a></td>
                    </tr>
                    <tr>
                      <td><a href="#"><small>7</small></a></td>
                      <td><a href="#"><small>8</small></a></td>
                      <td><a href="#"><small>9</small></a></td>
                      <td><a href="#"><small>10</small></a></td>
                      <td class="reservation-calendar_current-select"><a href="#"><small>11</small></a></td>
                      <td class="reservation-calendar_current-select"><a href="#"><small>12</small></a></td>
                      <td><a href="#"><small>13</small></a></td>
                    </tr>
                    <tr>
                      <td><a href="#"><small>14</small></a></td>
                      <td><a href="#"><small>15</small></a></td>
                      <td><a href="#"><small>16</small></a></td>
                      <td><a href="#"><small>17</small></a></td>
                      <td><a href="#"><small>18</small></a></td>
                      <td><a href="#"><small>19</small></a></td>
                      <td><a href="#"><small>20</small></a></td>
                    </tr>
                    <tr>
                      <td><a href="#"><small>21</small></a></td>
                      <td><a href="#"><small>22</small></a></td>
                      <td><a href="#"><small>23</small></a></td>
                      <td><a href="#"><small>24</small></a></td>
                      <td><a href="#"><small>25</small></a></td>
                      <td><a href="#"><small>26</small></a></td>
                      <td><a href="#"><small>27</small></a></td>
                    </tr>
                    <tr>
                      <td><a href="#"><small>28</small></a></td>
                      <td><a href="#"><small>29</small></a></td>
                      <td><a href="#"><small>30</small></a></td>
                      <td><a href="#"><small>31</small></a></td>
                      <td></td>
                      <td></td>
                      <td></td>
                    </tr>
                  </table>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
  <Footer></Footer>
</template>

<script>
import Footer from "@/components/Footer.vue";

export default {
    components: {
        Footer
    },
};
</script>

<style>
.header-text {
  display: flex;
  justify-content: center;
  align-items: center;
  margin-top: 220px;
}
</style>
