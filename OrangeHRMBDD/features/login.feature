#Author: your.email@your.domain.com
#Keywords Summary :
#Feature: List of scenarios.
#Scenario: Business rule through list of steps with arguments.
#Given: Some precondition step
#When: Some key actions
#Then: To observe outcomes or validation
#And,But: To enumerate more Given,When,Then steps
#Scenario Outline: List of steps for data-driven as an Examples and <placeholder>
#Examples: Container for s table
#Background: List of steps run before each of the scenarios
#""" (Doc Strings)
#| (Data Tables)
#@ (Tags/Labels):To group Scenarios
#<> (placeholder)
#""
## (Comments)
#Sample Feature Definition Template
@tag
Feature: Orange HRM Login Scenario

	@navigateToOrangeHrm
  Scenario: Navigation to OrangeHRM Site
    Given User launches chrome browser
    When User navigates to OrangeHRM Site
    Then Validate whether user landed in OrangeHRM Site
    
	@loginToOrangeHrm
	Scenario: Login to OrangeHRM Site
		Given User launches chrome browser
    When User navigates to OrangeHRM Site
    And User logs in to OrangeHRM Site
    Then User should be on Dashboard page
  
  @loginwithparameters
  Scenario: Login to OrangeHRM site with Parameters
  	Given User launches chrome browser
    When User navigates to OrangeHRM Site
    And User logs in to OrangeHRM Site with the Username "Admin1" and Password "admin"
    Then User should be on Dashboard page
    
  #@tag2
  #Scenario Outline: Title of your scenario outline
    #Given I want to write a step with <name>
    #When I check for the <value> in step
    #Then I verify the <status> in step
#
    #Examples: 
      #| name  | value | status  |
      #| name1 |     5 | success |
      #| name2 |     7 | Fail    |
