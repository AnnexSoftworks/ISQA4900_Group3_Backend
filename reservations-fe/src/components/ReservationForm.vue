<template>
  <div class="main-form">
    <base-dialog :show="showDialog" title="Form is invalid" @close="closeDialog">
      <p>Check-in and check-out date can't be empty</p>
    </base-dialog>
    <div class="booking-form">
      <div class="form-section" style="position: relative;" @click="checkInSelected">
        <button class="titles">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512"><!--! Font Awesome Pro 6.4.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2023 Fonticons, Inc. --><path d="M152 24c0-13.3-10.7-24-24-24s-24 10.7-24 24V64H64C28.7 64 0 92.7 0 128v16 48V448c0 35.3 28.7 64 64 64H384c35.3 0 64-28.7 64-64V192 144 128c0-35.3-28.7-64-64-64H344V24c0-13.3-10.7-24-24-24s-24 10.7-24 24V64H152V24zM48 192H400V448c0 8.8-7.2 16-16 16H64c-8.8 0-16-7.2-16-16V192z"/></svg>
          Check In
        </button>
        <p class="subtitle">{{ formatDate(dateFrom) }}</p>
      </div>

      <div class="partition"></div>

      <div class="form-section" @click="checkOutSelected">
        <button class="titles">
          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512"><!--! Font Awesome Pro 6.4.0 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license (Commercial License) Copyright 2023 Fonticons, Inc. --><path d="M152 24c0-13.3-10.7-24-24-24s-24 10.7-24 24V64H64C28.7 64 0 92.7 0 128v16 48V448c0 35.3 28.7 64 64 64H384c35.3 0 64-28.7 64-64V192 144 128c0-35.3-28.7-64-64-64H344V24c0-13.3-10.7-24-24-24s-24 10.7-24 24V64H152V24zM48 192H400V448c0 8.8-7.2 16-16 16H64c-8.8 0-16-7.2-16-16V192z"/></svg>
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

      <button class="search-button" @click="search">
        CHECK<br/>AVAILABILITY
      </button>
    </div>

    <transition name="datepicker">
      <div class="datepicker-checkin" v-if="showCheckInCalendar" v-click-outside="clickedOutside">
        <DatePicker
            class = "date-picker"
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
            class = "date-picker"
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
import { Calendar, DatePicker } from 'v-calendar';
import 'v-calendar/style.css';
import vClickOutside from "click-outside-vue3";

export default {
  name: "ReservationForm",
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
}
</script>

<style>

</style>