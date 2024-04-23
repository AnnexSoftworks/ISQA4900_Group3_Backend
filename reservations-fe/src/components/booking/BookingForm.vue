<template>
  <div class="main-form">
    <base-dialog :show="showDialog" title="Invalid Input" @close="closeDialog">
      <p>Error: Check-in and/or Check-out Date Cannot be Empty.</p>
    </base-dialog>
    <div class="booking-form">
      <div class="form-section" style="position: relative;" @click="checkInSelected">
        <button class="titles">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512">
            <!--! Font Awesome Pro 6.4.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2023 Fonticons, Inc. -->
            <path
                d="M152 24c0-13.3-10.7-24-24-24s-24 10.7-24 24V64H64C28.7 64 0 92.7 0 128v16 48V448c0 35.3 28.7 64 64 64H384c35.3 0 64-28.7 64-64V192 144 128c0-35.3-28.7-64-64-64H344V24c0-13.3-10.7-24-24-24s-24 10.7-24 24V64H152V24zM48 192H400V448c0 8.8-7.2 16-16 16H64c-8.8 0-16-7.2-16-16V192z"/>
          </svg>
          Check In
        </button>
        <p class="subtitle">{{ formatDate(dateFrom) }}</p>
      </div>

      <div class="partition"></div>

      <div class="form-section" @click="checkOutSelected">
        <button class="titles">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512">
            <!--! Font Awesome Pro 6.4.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2023 Fonticons, Inc. -->
            <path
                d="M152 24c0-13.3-10.7-24-24-24s-24 10.7-24 24V64H64C28.7 64 0 92.7 0 128v16 48V448c0 35.3 28.7 64 64 64H384c35.3 0 64-28.7 64-64V192 144 128c0-35.3-28.7-64-64-64H344V24c0-13.3-10.7-24-24-24s-24 10.7-24 24V64H152V24zM48 192H400V448c0 8.8-7.2 16-16 16H64c-8.8 0-16-7.2-16-16V192z"/>
          </svg>
          Check Out
        </button>
        <p class="subtitle">{{ formatDate(dateTo) }}</p>
      </div>

      <div class="partition"></div>

      <div class="form-section">
        <div class="counter-component">
          <button class="plus-minus" @click="decrementGuests">-</button>
          <p class="titles-for">Rooms For</p>
          <button class="plus-minus" @click="incrementGuests">+</button>
        </div>
        <p class="subtitle" v-if="totalGuests">Guests: {{ totalGuests }}</p>
      </div>

      <button class="search-button" @click="search" style="text-shadow: 1px 1px 3px rgb(0,0,0, 0.5);">
        CHECK<br/>AVAILABILITY
      </button>
    </div>

    <transition name="datepicker">
      <div class="datepicker-checkin" v-if="showCheckInCalendar" v-click-outside="clickedOutside">
        <DatePicker
            class="date-picker"
            @dayclick="handleDayClickIn"
            v-model="dateFrom"
            :min-date="getDatePlus(new Date(), 1)"
            :max-date="getDatePlus(new Date(), 60)"
            :is-dark="true">
        </DatePicker>
      </div>
    </transition>

    <transition name="datepicker">
      <div class="datepicker-checkout" v-if="showCheckOutCalendar" v-click-outside="clickedOutside">
        <DatePicker
            class="date-picker"
            @dayclick="handleDayClickOut"
            v-model="dateTo"
            :min-date="getDatePlus(this.dateFrom, 1) || getDatePlus(new Date(),2)"
            :max-date="getDatePlus(new Date(), 61)"
            :is-dark="true">
        </DatePicker>
      </div>
    </transition>
  </div>
</template>

<script>
import {Calendar, DatePicker} from 'v-calendar';
import 'v-calendar/style.css';
import vClickOutside from "click-outside-vue3";

export default {
  name: "TheBookingForm",
  components: {
    Calendar,
    DatePicker
  },
  data() {
    return {
      dateFrom: null,
      dateTo: null,
      showDialog: false,
      showCheckInCalendar: false,
      showCheckOutCalendar: false,
      checkIn: null,
      checkOut: null,
      totalGuests: 1,
    }
  },
  methods: {
    closeDialog() {
      this.showDialog = false;
    },
    getDatePlus(date, numberOfDays) {
      if (date === null) return null
      const newDate = new Date(date)
      newDate.setDate(newDate.getDate() + numberOfDays)
      return newDate
    },
    formatDate(date) {
      if (!date) return ''
      return `${date.getDate()} ${date.toLocaleString('default', {month: 'short'})} ${date.getFullYear()}`
    },
    checkInSelected() {
      if (this.showCheckInCalendar === true) {
        this.showCheckInCalendar = false;
        return;
      }
      this.showCheckInCalendar = true;
      this.showCheckOutCalendar = false;
    },
    checkOutSelected() {
      if (this.showCheckOutCalendar === true) {
        this.showCheckOutCalendar = false;
        return;
      }
      this.showCheckInCalendar = false;
      this.showCheckOutCalendar = true;
    },
    clickedOutside() {
      this.showCheckOutCalendar = false;
      this.showCheckInCalendar = false;
    },
    handleDayClickIn(day, event) {
      this.showCheckInCalendar = false;
      this.showCheckOutCalendar = false;
      if (this.dateTo === null) return
      if (this.dateTo > this.dateFrom) return
      this.dateTo = null
    },
    handleDayClickOut(day, event) {
      this.showCheckInCalendar = false;
      this.showCheckOutCalendar = false;
      if (this.dateFrom === null) return
      if (this.dateTo > this.dateFrom) return
      this.dateFrom = null
    },
    incrementGuests() {
      if (this.totalGuests < 6) {
        this.totalGuests++;
      }
    },
    decrementGuests() {
      if (this.totalGuests > 1) {
        this.totalGuests--;
      }
    },
    mounted() {
      this.changeDatePickerStyles();
    },
    search() {
      if (this.dateTo === null || this.dateFrom === null) {
        this.showDialog = true;
        return;
      }

      const startDate = this.getDatePlus(this.dateFrom, 1).toISOString().split('T')[0];
      const endDate = this.getDatePlus(this.dateTo, 1).toISOString().split('T')[0];

      this.$router.push({
        name: 'AvailableRooms',
        query: {
          start: startDate,
          end: endDate,
          totalGuests: this.totalGuests,
        },
      });
    },
    changeDatePickerStyles() {
      this.$nextTick(() => {
        // Change the background color of the title wrapper
        let titleWrappers = document.querySelectorAll('.vc-title-wrapper');
        titleWrappers.forEach(el => el.style.backgroundColor = 'lime'); // replace with your chosen color

        // Change the color of the arrow buttons
        let arrowButtons = document.querySelectorAll('.vc-header-nav button');
        arrowButtons.forEach(el => el.style.color = 'lime'); // replace with your chosen color
      });
    }
  },
  directives: {
    clickOutside: vClickOutside.directive
  },
}
</script>

<style scoped>
.subtitle {
  color: white;
  font-weight: 300;
  font-size: 12px;
  opacity: 0.6;
  margin-top: -12px;
}

.booking-form {
  opacity: 0.92;
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: rgba(28, 33, 45, 0.85);
  border-radius: 0;
  width: 900px;
  height: 70px;
  padding-top: 10px;
}

.form-section {
  flex: 1;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.partition {
  width: 0.2px;
  height: 90%;
  background-color: rgba(255, 255, 255, 0.5);
  align-self: center;
}

.search-button {
  border-radius: 0;
  transform: scale(1.2);
  width: 142px;
  height: 58px;
  padding-top: 0 !important;
  margin-top: -10px;
  background-color: #d7a500;
  line-height: 14px;
  font-size: 12px;
  font-weight: 500;
  color: #ffffff;
  border: none;
}

.datepicker-checkin {
  position: absolute;
  width: 100%;
  top: 75px;
  left: -310px;
}

.datepicker-checkout {
  position: absolute;
  width: 100%;
  top: 75px;
  left: -60px;
}

.date-picker {
  position: absolute;
  width: 100%;
  top: 0;
  left: 0;
}

.titles {
  display: flex;
  justify-content: center;
  align-items: center;
  color: white;
  font-size: 16px;
  margin-top: -10px;
  cursor: pointer;
  border: none;
  background-color: transparent;
}

.titles-for {
  display: flex;
  justify-content: center;
  align-items: center;
  color: white;
  font-size: 16px;
  padding: 1px 0 0 0;
  border: none;
  background-color: transparent;
}

.counter-component {
  display: flex;
  justify-content: center;
  align-items: center;
}

.plus-minus {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 30px;
  height: 30px;
  margin-left: 10px;
  margin-right: 10px;
  border-radius: 30%;
  background-color: transparent;
  color: white;
  font-size: 20px;
  font-weight: 500;
  cursor: pointer;
  border: none;
}

.plus-minus:hover {
  background-color: #d78f00;
  color: #1F232C;
}

.titles:hover {
  color: #d78f00;
}

.search-button:hover {
  color: black;
  background-color: white;
}

svg {
  fill: white;
  width: 15px;
  margin-right: 7px;
}

.search-svg {
  fill: #1F232C;
}

.datepicker-enter-from,
.datepicker-leave-to {
  transform: translateY(-10%);
  opacity: 0;
}

.datepicker-enter-active {
  transition: all 0.2s ease-in-out;
}

.datepicker-leave-active {
  transition: all 0.2s ease-in-out;
}

.datepicker-enter-to,
.datepicker-leave-from {
  transform: translateY(0);
  opacity: 1;
}

@media (max-width: 920px) {
  .booking-form {
    flex-direction: column; /* stack form sections vertically */
    width: 160px; /* auto width to fit mobile screens */
    height: 520px; /* adjust height to content */
  }

  .form-section {
    flex-direction: column;
    margin-top: 40px;
    margin-bottom: 40px; /* Add more space between form sections */
    height: 70px; /* Increase height of form sections */
    justify-content: space-between; /* distribute content of form sections */
    align-items: center; /* center content vertically */
  }

  .datepicker-checkout {
    top: 250px;
  }

  .datepicker-checkin {
    top: 100px;
  }

  .partition {
    width: 90%; /* adjust as needed */
    height: 0.1px; /* adjust as needed */
    background-color: white;
    align-self: center;
  }

  .datepicker-checkin, .datepicker-checkout {
    left: 0;
  }

  .search-button {
    transform: scale(1.4);
    width: 110px;
    height: 60px;
  }
}
</style>
