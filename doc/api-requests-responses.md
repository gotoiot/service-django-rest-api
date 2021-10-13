# Assesment

curl 'https://quiz-api.correlation-one.com/api/v1/test/data-scientist' \
  -H 'Connection: keep-alive' \
  -H 'sec-ch-ua: " Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'sec-ch-ua-mobile: ?1' \
  -H 'User-Agent: Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Mobile Safari/537.36' \
  -H 'Content-Type: application/json' \
  -H 'Origin: https://quiz.correlation-one.com' \
  -H 'Sec-Fetch-Site: same-site' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Referer: https://quiz.correlation-one.com/' \
  -H 'Accept-Language: en,es-ES;q=0.9,es;q=0.8' \
  --compressed

```json
{
    "Status": 1,
    "Message": "Ok",
    "Data": {
        "Id": 1251,
        "ParentTestId": 0,
        "TestType": 1,
        "Slug": "data-scientist",
        "Title": "Data Scientist",
        "Spot": "----",
        "VerifiedMobilePhone": false,
        "ThanksMessage": "Thanks for completing your assessment!",
        "Status": 1,
        "IsDeleted": false,
        "Configuration": {
            "Id": 0,
            "StartDate": "2021-04-27T02:07:37.577",
            "EndDate": "2026-04-27T02:07:37.577",
            "Duration": 60,
            "QuestionCount": 15,
            "Logo": "https://s3-us-west-2.amazonaws.com/correlation1-public/test_engine_assets/logo/correlation-one-07a22135-f7d9-4208-ad1e-b26eed3c10b2.png",
            "HeaderColor": "#01395f",
            "FooterColor": "#26425B",
            "FooterContent": "",
            "SkipQuestion": false,
            "SpecificQuestions": false,
            "ShowReviewPage": false,
            "AllowBlank": false,
            "BlankPoint": 0,
            "IsNotRandomQuestion": false,
            "IsNotRandomQuestionSortByIndex": false,
            "IsDownloadDetailReport": false,
            "IsPreventPII": false,
            "IsCollectFeedback": true,
            "DegreeEnabled": false,
            "IsNotifyEmail": false,
            "ToEmails": null,
            "FromEmail": null,
            "FromName": null,
            "EmailSubject": null,
            "EmailTemplate": null,
            "EmailParameters": null,
            "IsExperianTest": false,
            "ShowInstructions": true,
            "InstructionsText": "<h1 class=\"c1-auth-title\">Instructions:</h1> <div style=\"margin-bottom: 15px;\"><b style=\"display: inline-block;float: left;\">1. </b><span style=\"display: inline-block;width: 90%;padding-left: 15px;\">Do not use the back button on your browser.</span></div>\r  <div style=\"margin-bottom: 15px;\"><b style=\"display: inline-block;float: left;\">2. </b><span style=\"display: inline-block;width: 90%;padding-left: 15px;\">Do not navigate away from the browser session during the assessment.</span></div>\r  <div style=\"margin-bottom: 15px;\"><b style=\"display: inline-block;float: left;\">3. </b><span style=\"display: inline-block;width: 90%;padding-left: 15px;\">Complete the assessment in one session.</span></div>\r  <div style=\"margin-bottom: 15px;\"><b style=\"display: inline-block;float: left;\">4. </b><span style=\"display: inline-block;width: 90%;padding-left: 15px;\">Have a stable internet connection.</span></div>\r  <div style=\"margin-bottom: 25px;\"><b style=\"display: inline-block;float: left;\">5. </b><span style=\"display: inline-block;width: 90%;padding-left: 15px;\">Please note that it is not permitted to copy and/or publish any of the test content. Correlation One uses software which tracks and reports any copying which occurs during the test.</span></div>",
            "ShowTerms": false,
            "TermsText": null,
            "RequireConfirmation": false,
            "ConfirmationText": null,
            "IsNotifyCandidateEmail": false,
            "IsDisplayNotificationEmail": false,
            "CandidateEmailTemplate": null,
            "CandidateEmailParameters": null,
            "CandidateEmailSubject": null,
            "ShowPopStats": false,
            "IsCalcTestBenchmark": false,
            "IsExportAssessmentPDF": false,
            "IsAllowUserDetailPDF": false,
            "IsShowConfidenceQuestion": false,
            "Language": "en",
            "FromTemplateId": null,
            "HasIntegration": false,
            "IntegrationId": null,
            "RedirectTestId": null,
            "IsInviteOnly": false,
            "InviteOnlyAttempts": 0,
            "ShowWatermark": false
        },
        "Categories": null,
        "Degrees": null,
        "Taker": null,
        "TestAttemptsCount": 0,
        "AssessmentInfo": null,
        "Questions": null,
        "IsNotRandomQuestion": false,
        "IsNotRandomQuestionSortByIndex": false,
        "CustomTestId": 0
    }
}
```

# Create

curl 'https://quiz-api.correlation-one.com/api/v1/assessment/create/1251' \
  -H 'Connection: keep-alive' \
  -H 'sec-ch-ua: " Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'sec-ch-ua-mobile: ?1' \
  -H 'User-Agent: Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Mobile Safari/537.36' \
  -H 'Content-Type: application/json' \
  -H 'Origin: https://quiz.correlation-one.com' \
  -H 'Sec-Fetch-Site: same-site' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Referer: https://quiz.correlation-one.com/' \
  -H 'Accept-Language: en,es-ES;q=0.9,es;q=0.8' \
  --data-raw '{"Name":"Agustin","Surname":"Bassi","Email":"jagustinbassi@gmail.com","UId":"","MobilePhoneNumber":"","Datathon":"","Region":"","Language":"","CurrentPosition":"","CurrentAge":"","Gender":"","Experience":"","PracticeLocations":"","StatFamiliarity":"","GenericSkills":"","TerminalDegree":"","TerminalMajor":"","TerminalMinor":"","TerminalGradyear":"","TerminalGpa":"","TerminalOpportunities":"","TerminalSource":"","TerminalEngineeringSkills":"","TerminalMathhSkills":"","NotificationEmail":""}' \
  --compressed

```json
{
    "Status": 1,
    "Message": "Success",
    "Data": "097c03c9-b211-4195-8136-f5e91365e70f"
}
```

# Test

curl 'https://quiz-api.correlation-one.com/api/v1/assessment/097c03c9-b211-4195-8136-f5e91365e70f/test?tsp=1634129963271' \
  -H 'Connection: keep-alive' \
  -H 'sec-ch-ua: " Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'sec-ch-ua-mobile: ?1' \
  -H 'User-Agent: Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Mobile Safari/537.36' \
  -H 'Content-Type: application/json' \
  -H 'Origin: https://quiz.correlation-one.com' \
  -H 'Sec-Fetch-Site: same-site' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Referer: https://quiz.correlation-one.com/' \
  -H 'Accept-Language: en,es-ES;q=0.9,es;q=0.8' \
  --compressed

```json
{
    "Status": 1,
    "Message": "Ok",
    "Data": {
        "Id": 170914,
        "ParentTestId": 1251,
        "TestType": 0,
        "Slug": "data-scientist",
        "Title": "Data Scientist",
        "Spot": "----",
        "VerifiedMobilePhone": false,
        "ThanksMessage": "Thanks for completing your assessment!",
        "Status": 0,
        "IsDeleted": false,
        "Configuration": {
            "Id": 0,
            "StartDate": "2021-04-27T02:07:37.577",
            "EndDate": "2026-04-27T02:07:37.577",
            "Duration": 60,
            "QuestionCount": 15,
            "Logo": "https://s3-us-west-2.amazonaws.com/correlation1-public/test_engine_assets/logo/correlation-one-07a22135-f7d9-4208-ad1e-b26eed3c10b2.png",
            "HeaderColor": "#01395f",
            "FooterColor": "#26425B",
            "FooterContent": "",
            "SkipQuestion": false,
            "SpecificQuestions": false,
            "ShowReviewPage": false,
            "AllowBlank": false,
            "BlankPoint": 0,
            "IsNotRandomQuestion": false,
            "IsNotRandomQuestionSortByIndex": false,
            "IsDownloadDetailReport": false,
            "IsPreventPII": false,
            "IsCollectFeedback": true,
            "DegreeEnabled": false,
            "IsNotifyEmail": false,
            "ToEmails": null,
            "FromEmail": null,
            "FromName": null,
            "EmailSubject": null,
            "EmailTemplate": null,
            "EmailParameters": null,
            "IsExperianTest": false,
            "ShowInstructions": false,
            "InstructionsText": null,
            "ShowTerms": false,
            "TermsText": null,
            "RequireConfirmation": false,
            "ConfirmationText": null,
            "IsNotifyCandidateEmail": false,
            "IsDisplayNotificationEmail": false,
            "CandidateEmailTemplate": null,
            "CandidateEmailParameters": null,
            "CandidateEmailSubject": null,
            "ShowPopStats": false,
            "IsCalcTestBenchmark": false,
            "IsExportAssessmentPDF": false,
            "IsAllowUserDetailPDF": false,
            "IsShowConfidenceQuestion": false,
            "Language": null,
            "FromTemplateId": null,
            "HasIntegration": false,
            "IntegrationId": null,
            "RedirectTestId": null,
            "IsInviteOnly": false,
            "InviteOnlyAttempts": 0,
            "ShowWatermark": false
        },
        "Categories": null,
        "Degrees": null,
        "Taker": {
            "Id": 171051,
            "Email": "jagustinbassi@gmail.com",
            "Name": "Agustin",
            "Surname": "Bassi"
        },
        "TestAttemptsCount": 0,
        "AssessmentInfo": null,
        "Questions": null,
        "IsNotRandomQuestion": false,
        "IsNotRandomQuestionSortByIndex": false,
        "CustomTestId": 0
    }
}
```

# Start

curl 'https://quiz-api.correlation-one.com/api/v1/assessment/097c03c9-b211-4195-8136-f5e91365e70f/start' \
  -X 'POST' \
  -H 'Connection: keep-alive' \
  -H 'Content-Length: 0' \
  -H 'sec-ch-ua: " Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'sec-ch-ua-mobile: ?1' \
  -H 'User-Agent: Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Mobile Safari/537.36' \
  -H 'Content-Type: application/json' \
  -H 'Origin: https://quiz.correlation-one.com' \
  -H 'Sec-Fetch-Site: same-site' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Referer: https://quiz.correlation-one.com/' \
  -H 'Accept-Language: en,es-ES;q=0.9,es;q=0.8' \
  --compressed


```json
{
    "Status": 1,
    "Message": "Success",
    "Data": true
}
```

# Question 1

curl 'https://quiz-api.correlation-one.com/api/v1/assessment/097c03c9-b211-4195-8136-f5e91365e70f/question/1' \
  -H 'Connection: keep-alive' \
  -H 'sec-ch-ua: " Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'sec-ch-ua-mobile: ?1' \
  -H 'User-Agent: Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Mobile Safari/537.36' \
  -H 'Content-Type: application/json' \
  -H 'Origin: https://quiz.correlation-one.com' \
  -H 'Sec-Fetch-Site: same-site' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Referer: https://quiz.correlation-one.com/' \
  -H 'Accept-Language: en,es-ES;q=0.9,es;q=0.8' \
  --compressed


```json
{
    "Status": 1,
    "Message": "Success",
    "Data": {
        "Id": 2524930,
        "CategoryId": 0,
        "CategoryName": null,
        "QuestionType": 1,
        "Text": "<p>A study is conducted to review infant mortality rates at hospitals across the country. The study finds that, among the 10 hospitals with the lowest infant mortality rates, 8 of them were in rural counties. The rural hospitals were remote, often understaffed, and had a significantly lower volume of total patients than urban hospitals did.</p><p><br></p><p>Based on this study, which of the following conclusions would be MOST logical?</p>",
        "QuestionFile": null,
        "ChildQuestionText": null,
        "ChildQuestionText2": null,
        "ChildQuestionAnsweredText": null,
        "ChildQuestionAnsweredText2": null,
        "ActualDifficulty": 0,
        "Difficulty": 0,
        "MinValue": null,
        "MaxValue": null,
        "AnswerOptionId": null,
        "AnsweredText": null,
        "Score": null,
        "IsCorrect": null,
        "Status": 0,
        "Options": [
            {
                "Id": 11648378,
                "QuestionId": 0,
                "Text": "Infants in rural communities likely receive a higher degree of care, because there are fewer patients for the hospitals to serve",
                "Point": 0,
                "IsCorrect": null,
                "IsAnswer": null
            },
            {
                "Id": 11648379,
                "QuestionId": 0,
                "Text": "Among the 10 hospitals with the highest infant mortality rates, the majority are likely from rural counties",
                "Point": 0,
                "IsCorrect": null,
                "IsAnswer": null
            },
            {
                "Id": 11648380,
                "QuestionId": 0,
                "Text": "Infants in rural communities are healthier because of external factors, such as air quality, pollution, and diet",
                "Point": 0,
                "IsCorrect": null,
                "IsAnswer": null
            },
            {
                "Id": 11648381,
                "QuestionId": 0,
                "Text": "If urban hospitals studied rural hospitals and adopted their practices, they could provide better infant care",
                "Point": 0,
                "IsCorrect": null,
                "IsAnswer": null
            },
            {
                "Id": 11648382,
                "QuestionId": 0,
                "Text": "All of the above hypotheses are equally plausible",
                "Point": 0,
                "IsCorrect": null,
                "IsAnswer": null
            }
        ],
        "RemainingSecond": 3599.44,
        "EnvTag": 0,
        "IsPythonFile": false,
        "PythonFileId": null,
        "Category": null,
        "MasterQuestionId": 0,
        "IsMultiPart": false,
        "TotalShowCount": 0,
        "TotalCorrectCount": 0,
        "Percentage": 0
    }
}
```

# Answer 1

curl 'https://quiz-api.correlation-one.com/api/v1/assessment/097c03c9-b211-4195-8136-f5e91365e70f/answer' \
  -H 'Connection: keep-alive' \
  -H 'sec-ch-ua: " Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'sec-ch-ua-mobile: ?1' \
  -H 'User-Agent: Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Mobile Safari/537.36' \
  -H 'Content-Type: application/json' \
  -H 'Origin: https://quiz.correlation-one.com' \
  -H 'Sec-Fetch-Site: same-site' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Referer: https://quiz.correlation-one.com/' \
  -H 'Accept-Language: en,es-ES;q=0.9,es;q=0.8' \
  --data-raw 
```json
{
    "QuestionId": 2524930,
    "OptionId": "11648379",
    "AnsweredText": null,
    "ChildQuestionAnsweredText": null,
    "ChildQuestionAnsweredText2": null
}
```

```json
{
    "Status": 1,
    "Message": "Success",
    "Data": true
}
```

# Question 15

curl 'https://quiz-api.correlation-one.com/api/v1/assessment/097c03c9-b211-4195-8136-f5e91365e70f/question/15' \
  -H 'Connection: keep-alive' \
  -H 'sec-ch-ua: " Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'sec-ch-ua-mobile: ?1' \
  -H 'User-Agent: Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Mobile Safari/537.36' \
  -H 'Content-Type: application/json' \
  -H 'Origin: https://quiz.correlation-one.com' \
  -H 'Sec-Fetch-Site: same-site' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Referer: https://quiz.correlation-one.com/' \
  -H 'Accept-Language: en,es-ES;q=0.9,es;q=0.8' \
  --compressed

```json
{
    "Status": 1,
    "Message": "Success",
    "Data": {
        "Id": 2524944,
        "CategoryId": 0,
        "CategoryName": null,
        "QuestionType": 1,
        "Text": "You are tuning a linear classifier that you suspect is overfitting your data. Which of the following is MOST likely to make the overfitting worse?",
        "QuestionFile": null,
        "ChildQuestionText": null,
        "ChildQuestionText2": null,
        "ChildQuestionAnsweredText": null,
        "ChildQuestionAnsweredText2": null,
        "ActualDifficulty": 0,
        "Difficulty": 0,
        "MinValue": null,
        "MaxValue": null,
        "AnswerOptionId": null,
        "AnsweredText": null,
        "Score": null,
        "IsCorrect": null,
        "Status": 0,
        "Options": [
            {
                "Id": 11648446,
                "QuestionId": 0,
                "Text": "Using <img alt=\"k\" src=\"https://s3.amazonaws.com/c1-latex/6fe0ce1e0d124ae0acd6b5209d28feb8-option-13806-1.gif\"> - fold cross-validation",
                "Point": 0,
                "IsCorrect": null,
                "IsAnswer": null
            },
            {
                "Id": 11648447,
                "QuestionId": 0,
                "Text": "Acquiring more data points",
                "Point": 0,
                "IsCorrect": null,
                "IsAnswer": null
            },
            {
                "Id": 11648448,
                "QuestionId": 0,
                "Text": "Applying a more stringent regularization on the features",
                "Point": 0,
                "IsCorrect": null,
                "IsAnswer": null
            },
            {
                "Id": 11648449,
                "QuestionId": 0,
                "Text": "Decreasing the number of features",
                "Point": 0,
                "IsCorrect": null,
                "IsAnswer": null
            },
            {
                "Id": 11648450,
                "QuestionId": 0,
                "Text": "Increasing the number of features",
                "Point": 0,
                "IsCorrect": null,
                "IsAnswer": null
            }
        ],
        "RemainingSecond": 3385.747,
        "EnvTag": 0,
        "IsPythonFile": false,
        "PythonFileId": null,
        "Category": null,
        "MasterQuestionId": 0,
        "IsMultiPart": false,
        "TotalShowCount": 0,
        "TotalCorrectCount": 0,
        "Percentage": 0
    }
}
```

# Answer 15

curl 'https://quiz-api.correlation-one.com/api/v1/assessment/097c03c9-b211-4195-8136-f5e91365e70f/answer' \
  -H 'Connection: keep-alive' \
  -H 'sec-ch-ua: " Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'sec-ch-ua-mobile: ?1' \
  -H 'User-Agent: Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Mobile Safari/537.36' \
  -H 'Content-Type: application/json' \
  -H 'Origin: https://quiz.correlation-one.com' \
  -H 'Sec-Fetch-Site: same-site' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Referer: https://quiz.correlation-one.com/' \
  -H 'Accept-Language: en,es-ES;q=0.9,es;q=0.8' \
  --data-raw 
  ```json
{
    "QuestionId": 2524944,
    "OptionId": "11648450",
    "AnsweredText": null,
    "ChildQuestionAnsweredText": null,
    "ChildQuestionAnsweredText2": null
}
```

```json
{
    "Status": 1,
    "Message": "Success",
    "Data": true
}
```

# End

curl 'https://quiz-api.correlation-one.com/api/v1/assessment/097c03c9-b211-4195-8136-f5e91365e70f/end' \
  -X 'POST' \
  -H 'Connection: keep-alive' \
  -H 'Content-Length: 0' \
  -H 'sec-ch-ua: " Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'sec-ch-ua-mobile: ?1' \
  -H 'User-Agent: Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Mobile Safari/537.36' \
  -H 'Content-Type: application/json' \
  -H 'Origin: https://quiz.correlation-one.com' \
  -H 'Sec-Fetch-Site: same-site' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Referer: https://quiz.correlation-one.com/' \
  -H 'Accept-Language: en,es-ES;q=0.9,es;q=0.8' \
  --compressed

```json
{
    "Status": 1,
    "Message": "Success",
    "Data": true
}
```

# Result

curl 'https://quiz-api.correlation-one.com/api/v1/assessment/097c03c9-b211-4195-8136-f5e91365e70f/result' \
  -H 'Connection: keep-alive' \
  -H 'sec-ch-ua: " Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'sec-ch-ua-mobile: ?1' \
  -H 'User-Agent: Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Mobile Safari/537.36' \
  -H 'Content-Type: application/json' \
  -H 'Origin: https://quiz.correlation-one.com' \
  -H 'Sec-Fetch-Site: same-site' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Referer: https://quiz.correlation-one.com/' \
  -H 'Accept-Language: en,es-ES;q=0.9,es;q=0.8' \
  --compressed

```json
{
    "Status": 1,
    "Message": "Success",
    "Data": {
        "Id": 170916,
        "TestType": 1,
        "ClientUserId": null,
        "GKey": "097c03c9-b211-4195-8136-f5e91365e70f",
        "TakerId": 171051,
        "TakerName": "Agustin",
        "TakerSurname": "Bassi",
        "TakerEmail": "jagustinbassi@gmail.com",
        "MobilePhone": "",
        "Region": null,
        "UserConfidenceScore": 0.0,
        "QuestionCount": 15,
        "CorrectTotalScore": 15,
        "AssessmentTotalScore": 80,
        "EmptyAnswers": 0,
        "CorrectAnswers": 3,
        "InCorrectAnswers": 12,
        "TimeTaken": "3 minutes, 43 seconds, 403 milliseconds",
        "StartDate": "2021-10-13T12:59:24.187",
        "EndDate": "2021-10-13T13:03:07.59",
        "CreatedDate": "2021-10-13T12:59:22.99",
        "IpAddress": "138.117.48.63",
        "DegreeText": "Bronze",
        "Categories": [
            {
                "CategoryName": "Bayesian Probability",
                "QuestionCount": 1,
                "Correct": 0,
                "InCorrect": 1,
                "Empty": 0,
                "CorrectTotalScore": 0,
                "TotalScore": 5
            },
            {
                "CategoryName": "Classification Models",
                "QuestionCount": 2,
                "Correct": 0,
                "InCorrect": 2,
                "Empty": 0,
                "CorrectTotalScore": 0,
                "TotalScore": 10
            },
            {
                "CategoryName": "Data Visualization",
                "QuestionCount": 1,
                "Correct": 0,
                "InCorrect": 1,
                "Empty": 0,
                "CorrectTotalScore": 0,
                "TotalScore": 5
            },
            {
                "CategoryName": "Data Wrangling & Cleaning",
                "QuestionCount": 2,
                "Correct": 1,
                "InCorrect": 1,
                "Empty": 0,
                "CorrectTotalScore": 5,
                "TotalScore": 15
            },
            {
                "CategoryName": "Distributions",
                "QuestionCount": 1,
                "Correct": 0,
                "InCorrect": 1,
                "Empty": 0,
                "CorrectTotalScore": 0,
                "TotalScore": 5
            },
            {
                "CategoryName": "Interpretation of Charts, Graphs & Tables",
                "QuestionCount": 1,
                "Correct": 0,
                "InCorrect": 1,
                "Empty": 0,
                "CorrectTotalScore": 0,
                "TotalScore": 5
            },
            {
                "CategoryName": "Linear Modeling",
                "QuestionCount": 4,
                "Correct": 0,
                "InCorrect": 4,
                "Empty": 0,
                "CorrectTotalScore": 0,
                "TotalScore": 20
            },
            {
                "CategoryName": "Overfitting, Underfitting & Cross-Validation",
                "QuestionCount": 1,
                "Correct": 1,
                "InCorrect": 0,
                "Empty": 0,
                "CorrectTotalScore": 5,
                "TotalScore": 5
            },
            {
                "CategoryName": "Statistical Inference",
                "QuestionCount": 2,
                "Correct": 1,
                "InCorrect": 1,
                "Empty": 0,
                "CorrectTotalScore": 5,
                "TotalScore": 10
            }
        ],
        "ChildQuestionCategories": [],
        "RqAssessmentScore": null,
        "AssessmentScore211": null,
        "AssessmentSectionScoreDetail": null,
        "RedirectToNewAssessment": null
    }
}
```
