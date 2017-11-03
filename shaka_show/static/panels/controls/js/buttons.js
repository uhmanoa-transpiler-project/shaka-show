console.log('entered controls/buttons.js');

import { getXSRFCookie } from '../../../utils';

define([
  'jquery'
], function($) {

  // API urls for runtime control buttons
  const start_url = '/ajax/controls/buttons/start';
  const pause_url = '/ajax/controls/buttons/pause';
  const stop_url  = '/ajax/controls/buttons/stop';
  const step_url  = '/ajax/controls/buttons/step';
  const xsrf_data = $.param({_xsrf: getXSRFCookie()});

  // Add Shaka-Show API requests to button clicks
  $(document).ready(function() {


    // Start button
    $('#start-button').click(function(event) {
      event.preventDefault();

      $.ajax({
        url: start_url,
        type: 'POST',
        data: xsrf_data,
        dataType: 'text',
        success(response) {
          console.log('controls: start btn post success');
          console.log(response);
        },
        error() {
          console.log('controls: start btn post failure');
        }
      });
    });


    // Pause button
    $('#pause-button').click(function(event) {
      event.preventDefault();

      $.ajax({
        url: pause_url,
        type: 'POST',
        data: xsrf_data,
        dataType: 'text',
        success(response) {
          console.log('controls: pause btn post success');
          console.log(response);
        },
        error() {
          console.log('controls: pause btn post failure');
        }
      });
    });


    // Stop button
    $('#stop-button').click(function(event) {
      event.preventDefault();
      $.ajax({
        url: stop_url,
        type: 'POST',
        data: xsrf_data,
        dataType: 'text',
        success(response) {
          console.log('controls: stop btn post success');
          console.log(response);
        },
        error() {
          console.log('controls: stop btn post failure');
        }
      });
    });


    // Step button
    $('#step-button').click(function(event) {
      event.preventDefault();
      $.ajax({
        url: step_url,
        type: 'POST',
        data: xsrf_data,
        dataType: 'text',
        success(response) {
          console.log('controls: step btn post success');
          console.log(response);
        },
        error() {
          console.log('controls: step btn post failure');
        }
      });
    });


  });
});

