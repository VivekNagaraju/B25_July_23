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
@LoginFeature
Feature: Orange HRM Login Scenario

	Background: Pre-condtion steps for Login Scenarios
		Given User launches chrome browser
    When User navigates to OrangeHRM Site
	
	@navigateToOrangeHrm @sanity
  Scenario: Navigation to OrangeHRM Site
    Then Validate whether user landed in OrangeHRM Site
    
	@loginToOrangeHrm @sanity
	Scenario: Login to OrangeHRM Site
    When User logs in to OrangeHRM Site
    Then User should be on Dashboard page
  
  @loginwithparameters @regression
  Scenario: Login to OrangeHRM site with Parameters
    When User logs in to OrangeHRM Site with the Username "Admin" and Password "admin123"
    Then User should be on Dashboard page
    
   @LoginDDT @regression
   Scenario Outline: Login to OrangeHRM- Data Driven Testing 
	    When User logs in to OrangeHRM Site with the Username "<UserName>" and Password "<PassWord>"
	    Then User should be on Dashboard page
    
    Examples:
    |UserName|PassWord|
    |Admin|admin123|
    |Admin|admin1234|
    |Admin1|admin123|
    
    
    
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
