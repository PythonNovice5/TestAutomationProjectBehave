Feature: Verify Sort and Filter

    Background:
        Given I launch "Chrome" browser
        When I goto "https://mystifying-beaver-ee03b5.netlify.app" url
        When I store the original values for comparison

    Scenario Outline: Verify if the Filter and Sort are working correctly for any data
    When I enter "<filter_input>" into Filter Data
    And I verify that all records related to "<filter_input>" are returned
    When I select "Impact score" from SortData dropdown
    Then I verify that records are sorted by "Impact score"
    When I select "Number of cases" from SortData dropdown
    Then I verify that records are sorted by "Number of cases"
    When I select "Name" from SortData dropdown
    Then I verify that records are sorted by "Name"
    When I select "Complexity" from SortData dropdown
    Then I verify that records are sorted by "Complexity"
    And I close the browser
    Examples:
      |filter_input|
      |high        |
      |low         |
      |Phishing    |
      |phishing    |
      |xss          |
      |PASSWORD ATTACK   |