# Assesment

## Request

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

## Response

```json
{"Status":1,"Message":"Ok","Data":{"Id":1251,"ParentTestId":0,"TestType":1,"Slug":"data-scientist","Title":"Data Scientist","Spot":"----","VerifiedMobilePhone":false,"ThanksMessage":"Thanks for completing your assessment!","Status":1,"IsDeleted":false,"Configuration":{"Id":0,"StartDate":"2021-04-27T02:07:37.577","EndDate":"2026-04-27T02:07:37.577","Duration":60,"QuestionCount":15,"Logo":"https://s3-us-west-2.amazonaws.com/correlation1-public/test_engine_assets/logo/correlation-one-07a22135-f7d9-4208-ad1e-b26eed3c10b2.png","HeaderColor":"#01395f","FooterColor":"#26425B","FooterContent":"","SkipQuestion":false,"SpecificQuestions":false,"ShowReviewPage":false,"AllowBlank":false,"BlankPoint":0,"IsNotRandomQuestion":false,"IsNotRandomQuestionSortByIndex":false,"IsDownloadDetailReport":false,"IsPreventPII":false,"IsCollectFeedback":true,"DegreeEnabled":false,"IsNotifyEmail":false,"ToEmails":null,"FromEmail":null,"FromName":null,"EmailSubject":null,"EmailTemplate":null,"EmailParameters":null,"IsExperianTest":false,"ShowInstructions":true,"InstructionsText":"<h1 class=\"c1-auth-title\">Instructions:</h1> <div style=\"margin-bottom: 15px;\"><b style=\"display: inline-block;float: left;\">1. </b><span style=\"display: inline-block;width: 90%;padding-left: 15px;\">Do not use the back button on your browser.</span></div>\r  <div style=\"margin-bottom: 15px;\"><b style=\"display: inline-block;float: left;\">2. </b><span style=\"display: inline-block;width: 90%;padding-left: 15px;\">Do not navigate away from the browser session during the assessment.</span></div>\r  <div style=\"margin-bottom: 15px;\"><b style=\"display: inline-block;float: left;\">3. </b><span style=\"display: inline-block;width: 90%;padding-left: 15px;\">Complete the assessment in one session.</span></div>\r  <div style=\"margin-bottom: 15px;\"><b style=\"display: inline-block;float: left;\">4. </b><span style=\"display: inline-block;width: 90%;padding-left: 15px;\">Have a stable internet connection.</span></div>\r  <div style=\"margin-bottom: 25px;\"><b style=\"display: inline-block;float: left;\">5. </b><span style=\"display: inline-block;width: 90%;padding-left: 15px;\">Please note that it is not permitted to copy and/or publish any of the test content. Correlation One uses software which tracks and reports any copying which occurs during the test.</span></div>","ShowTerms":false,"TermsText":null,"RequireConfirmation":false,"ConfirmationText":null,"IsNotifyCandidateEmail":false,"IsDisplayNotificationEmail":false,"CandidateEmailTemplate":null,"CandidateEmailParameters":null,"CandidateEmailSubject":null,"ShowPopStats":false,"IsCalcTestBenchmark":false,"IsExportAssessmentPDF":false,"IsAllowUserDetailPDF":false,"IsShowConfidenceQuestion":false,"Language":"en","FromTemplateId":null,"HasIntegration":false,"IntegrationId":null,"RedirectTestId":null,"IsInviteOnly":false,"InviteOnlyAttempts":0,"ShowWatermark":false},"Categories":null,"Degrees":null,"Taker":null,"TestAttemptsCount":0,"AssessmentInfo":null,"Questions":null,"IsNotRandomQuestion":false,"IsNotRandomQuestionSortByIndex":false,"CustomTestId":0}}
```

# Create assesment

## Request

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

## Response

{"Status":1,"Message":"Success","Data":"f36b02d1-854c-48c7-8a89-785b84f9c1f7"}

# Test

## Request

curl 'https://quiz-api.correlation-one.com/api/v1/assessment/f36b02d1-854c-48c7-8a89-785b84f9c1f7/test?tsp=1633453015526' \
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

## Response

{"Status":1,"Message":"Ok","Data":{"Id":170065,"ParentTestId":1251,"TestType":0,"Slug":"data-scientist","Title":"Data Scientist","Spot":"----","VerifiedMobilePhone":false,"ThanksMessage":"Thanks for completing your assessment!","Status":0,"IsDeleted":false,"Configuration":{"Id":0,"StartDate":"2021-04-27T02:07:37.577","EndDate":"2026-04-27T02:07:37.577","Duration":60,"QuestionCount":15,"Logo":"https://s3-us-west-2.amazonaws.com/correlation1-public/test_engine_assets/logo/correlation-one-07a22135-f7d9-4208-ad1e-b26eed3c10b2.png","HeaderColor":"#01395f","FooterColor":"#26425B","FooterContent":"","SkipQuestion":false,"SpecificQuestions":false,"ShowReviewPage":false,"AllowBlank":false,"BlankPoint":0,"IsNotRandomQuestion":false,"IsNotRandomQuestionSortByIndex":false,"IsDownloadDetailReport":false,"IsPreventPII":false,"IsCollectFeedback":true,"DegreeEnabled":false,"IsNotifyEmail":false,"ToEmails":null,"FromEmail":null,"FromName":null,"EmailSubject":null,"EmailTemplate":null,"EmailParameters":null,"IsExperianTest":false,"ShowInstructions":false,"InstructionsText":null,"ShowTerms":false,"TermsText":null,"RequireConfirmation":false,"ConfirmationText":null,"IsNotifyCandidateEmail":false,"IsDisplayNotificationEmail":false,"CandidateEmailTemplate":null,"CandidateEmailParameters":null,"CandidateEmailSubject":null,"ShowPopStats":false,"IsCalcTestBenchmark":false,"IsExportAssessmentPDF":false,"IsAllowUserDetailPDF":false,"IsShowConfidenceQuestion":false,"Language":null,"FromTemplateId":null,"HasIntegration":false,"IntegrationId":null,"RedirectTestId":null,"IsInviteOnly":false,"InviteOnlyAttempts":0,"ShowWatermark":false},"Categories":null,"Degrees":null,"Taker":{"Id":170202,"Email":"jagustinbassi@gmail.com","Name":"Agustin","Surname":"Bassi"},"TestAttemptsCount":0,"AssessmentInfo":null,"Questions":null,"IsNotRandomQuestion":false,"IsNotRandomQuestionSortByIndex":false,"CustomTestId":0}}

# Start assesment

## Request

curl 'https://quiz-api.correlation-one.com/api/v1/assessment/f36b02d1-854c-48c7-8a89-785b84f9c1f7/start' \
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

## Response

{"Status":1,"Message":"Success","Data":true}

# Health

## Request

curl 'https://quiz-api.correlation-one.com/api/v1/assessment/healthz' \
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

## Response

{"Status":1,"Message":"Success","Data":200}

# Next question

## Request

curl 'https://quiz-api.correlation-one.com/api/v1/assessment/f36b02d1-854c-48c7-8a89-785b84f9c1f7/question/2' \
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

## Response

{"Status":1,"Message":"Success","Data":{"Id":2515387,"CategoryId":0,"CategoryName":null,"QuestionType":1,"Text":"<p>You are a sales manager trying to prioritize limited resources, and have access to a data table which shows the number of sales leads and closed sales across all customer segments for three products, <span class=\"ql-formula\" data-value=\"A, B, C\">﻿<span contenteditable=\"false\"><span class=\"katex\"><span class=\"katex-mathml\"><math><semantics><mrow><mi>A</mi><mo separator=\"true\">,</mo><mi>B</mi><mo separator=\"true\">,</mo><mi>C</mi></mrow><annotation encoding=\"application/x-tex\">A, B, C</annotation></semantics></math></span><span class=\"katex-html\" aria-hidden=\"true\"><span class=\"base\"><span class=\"strut\" style=\"height: 0.8777699999999999em; vertical-align: -0.19444em;\"></span><span class=\"mord mathdefault\">A</span><span class=\"mpunct\">,</span><span class=\"mspace\" style=\"margin-right: 0.16666666666666666em;\"></span><span class=\"mord mathdefault\" style=\"margin-right: 0.05017em;\">B</span><span class=\"mpunct\">,</span><span class=\"mspace\" style=\"margin-right: 0.16666666666666666em;\"></span><span class=\"mord mathdefault\" style=\"margin-right: 0.07153em;\">C</span></span></span></span></span>﻿</span>. Based on the given data, choose the option that describes the BEST course of action to improve sales efficiency across all segments:</p><p><br></p><p><img src=\"https://s3.us-east-2.amazonaws.com/c1-questions/3197.png\" alt=\"Sales Lead &amp; Closed Sales Table\"></p>","QuestionFile":null,"ChildQuestionText":null,"ChildQuestionText2":null,"ChildQuestionAnsweredText":null,"ChildQuestionAnsweredText2":null,"ActualDifficulty":0,"Difficulty":0,"MinValue":null,"MaxValue":null,"AnswerOptionId":null,"AnsweredText":null,"Score":null,"IsCorrect":null,"Status":0,"Options":[{"Id":11603876,"QuestionId":0,"Text":"Have your sales team only promote product <img alt=\"A\" src=\"https://s3.amazonaws.com/c1-latex/da6276493789402e926ca367b6594d3a-option-19964-1.gif\">","Point":0,"IsCorrect":null,"IsAnswer":null},{"Id":11603877,"QuestionId":0,"Text":"Have your sales team only promote products <img alt=\"A\" src=\"https://s3.amazonaws.com/c1-latex/260263b39ffa428a9d23978a43ad2a50-option-19965-1.gif\"> and <img alt=\"C\" src=\"https://s3.amazonaws.com/c1-latex/7ebd425a586c4afbad9dd63ff27317c7-option-19965-2.gif\">","Point":0,"IsCorrect":null,"IsAnswer":null},{"Id":11603878,"QuestionId":0,"Text":"Have your sales team only promote product <img alt=\"B\" src=\"https://s3.amazonaws.com/c1-latex/12bc3acb4ae4496aa89e14bdfa25ba14-option-19966-1.gif\">","Point":0,"IsCorrect":null,"IsAnswer":null},{"Id":11603879,"QuestionId":0,"Text":"Have your sales team only promote products <img alt=\"B\" src=\"https://s3.amazonaws.com/c1-latex/3f7424a524ce4abf907902baeae5ed7b-option-19967-1.gif\"> and <img alt=\"C\" src=\"https://s3.amazonaws.com/c1-latex/f64a5b33320a41778935fe6beb876dc3-option-19967-2.gif\">","Point":0,"IsCorrect":null,"IsAnswer":null},{"Id":11603880,"QuestionId":0,"Text":"Have your sales team promote all three products equally","Point":0,"IsCorrect":null,"IsAnswer":null}],"RemainingSecond":3440.9199999999996,"EnvTag":0,"IsPythonFile":false,"PythonFileId":null,"Category":null,"MasterQuestionId":0,"IsMultiPart":false,"TotalShowCount":0,"TotalCorrectCount":0,"Percentage":0}}

# End assesment

## Request

curl 'https://quiz-api.correlation-one.com/api/v1/assessment/f36b02d1-854c-48c7-8a89-785b84f9c1f7/end' \
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

## Response

{"Status":1,"Message":"Success","Data":true}

# Assesment result

## Request

curl 'https://quiz-api.correlation-one.com/api/v1/assessment/f36b02d1-854c-48c7-8a89-785b84f9c1f7/result' \
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

## Response

{"Status":1,"Message":"Success","Data":{"Id":170067,"TestType":1,"ClientUserId":null,"GKey":"f36b02d1-854c-48c7-8a89-785b84f9c1f7","TakerId":170202,"TakerName":"Agustin","TakerSurname":"Bassi","TakerEmail":"jagustinbassi@gmail.com","MobilePhone":"","Region":null,"UserConfidenceScore":0.0,"QuestionCount":15,"CorrectTotalScore":0,"AssessmentTotalScore":80,"EmptyAnswers":14,"CorrectAnswers":0,"InCorrectAnswers":1,"TimeTaken":"60 minutes, 113 milliseconds","StartDate":"2021-10-05T16:56:56.38","EndDate":"2021-10-05T17:56:56.493","CreatedDate":"2021-10-05T16:56:55.17","IpAddress":"138.117.48.63","DegreeText":"Bronze","Categories":[{"CategoryName":"Bayesian Probability","QuestionCount":1,"Correct":0,"InCorrect":0,"Empty":1,"CorrectTotalScore":0,"TotalScore":5},{"CategoryName":"Classification Models","QuestionCount":2,"Correct":0,"InCorrect":0,"Empty":2,"CorrectTotalScore":0,"TotalScore":10},{"CategoryName":"Data Visualization","QuestionCount":1,"Correct":0,"InCorrect":0,"Empty":1,"CorrectTotalScore":0,"TotalScore":5},{"CategoryName":"Data Wrangling & Cleaning","QuestionCount":2,"Correct":0,"InCorrect":0,"Empty":2,"CorrectTotalScore":0,"TotalScore":15},{"CategoryName":"Distributions","QuestionCount":1,"Correct":0,"InCorrect":0,"Empty":1,"CorrectTotalScore":0,"TotalScore":5},{"CategoryName":"Interpretation of Charts, Graphs & Tables","QuestionCount":1,"Correct":0,"InCorrect":0,"Empty":1,"CorrectTotalScore":0,"TotalScore":5},{"CategoryName":"Linear Modeling","QuestionCount":4,"Correct":0,"InCorrect":0,"Empty":4,"CorrectTotalScore":0,"TotalScore":20},{"CategoryName":"Overfitting, Underfitting & Cross-Validation","QuestionCount":1,"Correct":0,"InCorrect":0,"Empty":1,"CorrectTotalScore":0,"TotalScore":5},{"CategoryName":"Statistical Inference","QuestionCount":2,"Correct":0,"InCorrect":1,"Empty":1,"CorrectTotalScore":0,"TotalScore":10}],"ChildQuestionCategories":[],"RqAssessmentScore":null,"AssessmentScore211":null,"AssessmentSectionScoreDetail":null,"RedirectToNewAssessment":null}}

# False ?

## Request

curl 'https://quiz-api.correlation-one.com/api/v1/survey/testBySlug/data-scientist/false' \
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

## Response

{"Status":1,"Message":"Success","Data":[]}
