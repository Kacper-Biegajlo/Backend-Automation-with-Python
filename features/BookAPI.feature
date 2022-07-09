# Created by kacperbiegajlo at 05/07/2022
Feature: Verify if Books are added and deleted using Library API
  # Enter feature description here

  @library
  Scenario: Verify AddBook API functionality
    Given the Book details which needs to be added to Library
    When we execute the AddBook Post API method
    Then the Book is successfully added
    And status code of response should be 200

  @library
  Scenario Outline: Verify AddBook API functionality
    Given the Book details with <isbn> and <aisle>
    When we execute the AddBook Post API method
    Then the Book is successfully added
      Examples:
        | isbn  | aisle |
        | Pog4   | 6962  |
        | Sadge4 | 42321 |

