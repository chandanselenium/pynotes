*** Settings ***
Documentation  Script to add product to cart
Library  SeleniumLibrary

*** Test Cases ***
test case 1 for amazon
  [Documentation]    this is a script to select the product and add to cart
  [Tags]  Smoke
  #open the browser
  Open Browser  http://www.amazon.in  chrome
  sleep  5s
  #wait till you get ==> 'your amazon.in'
  Wait Until Page Contains  Your Amazon.in
  #inspect search text field and enter 'readmi 7a'
  Input Text  id=twotabsearchtextbox  readmi 7a
  #inspect search button and click on it
  Click Button  xpath=//div[@class='nav-search-submit nav-sprite']//input[@class='nav-input']
  #click on mobile link
  Click Link  -c.a-aui_perf_130093-c.a-aui_tnr_v2_180836-c.a-aui_ux_145937-c.a-meter-animate:nth-child(2) div.sg-row:nth-child(4) div.sg-col-20-of-24.sg-col-28-of-32.sg-col-16-of-20.sg-col.s-right-column.sg-col-32-of-36.sg-col-8-of-12.sg-col-12-of-16.sg-col-24-of-28 div.sg-col-inner span.rush-component.s-latency-cf-section:nth-child(4) div.s-result-list.s-search-results.sg-row div.sg-col-20-of-24.s-result-item.sg-col-0-of-12.sg-col-28-of-32.sg-col-16-of-20.sg-col.sg-col-32-of-36.sg-col-12-of-16.sg-col-24-of-28:nth-child(1) div.sg-col-inner div.s-include-content-margin.s-border-bottom div.a-section.a-spacing-medium div.sg-row:nth-child(2) div.sg-col-4-of-12.sg-col-8-of-16.sg-col-16-of-24.sg-col-12-of-20.sg-col-24-of-32.sg-col.sg-col-28-of-36.sg-col-20-of-28 div.sg-col-inner div.sg-row:nth-child(1) div.sg-col-4-of-12.sg-col-8-of-16.sg-col-12-of-32.sg-col-12-of-20.sg-col-12-of-36.sg-col.sg-col-12-of-24.sg-col-12-of-28 div.sg-col-inner div.a-section.a-spacing-none h2.a-size-mini.a-spacing-none.a-color-base.s-line-clamp-2 > a.a-link-normal.a-text-normal
  Sleep  5s
  #wait till you get 'back to result'
  Wait Until Page Contains  Back to results
  #click on add to cart
  Click Button  id=add-to-cart-button
  #wait till you get add to cart
  Wait Until Page Contains  add to cart
  Click Link  id=
  Page Should Contain Element  continue
  Close Browser



