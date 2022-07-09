
Feature: Github API validation
  # Enter feature description here

  Scenario: Session managment check
    Given I have github auth credentials
    When I hit getRepository API of github
    Then status code of response should be 200
