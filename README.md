[comment]: # "Auto-generated SOAR connector documentation"
# Falcon Sandbox

Publisher: Hybrid Analysis  
Connector Version: 1\.1\.7  
Product Vendor: Hybrid Analysis  
Product Name: Falcon Sandbox  
Product Version Supported (regex): "\.\*"  
Minimum Product Version: 3\.5\.180  

This app integrates with Falcon Sandbox Services to provide investigative actions

[comment]: # " File: readme.md"
[comment]: # "  Licensed under Apache 2.0 (https://www.apache.org/licenses/LICENSE-2.0.txt)"
[comment]: # ""
##### Usage

Should you not be using hybrid-analysis.com as the application server, but a private cloud or on
premise instance, please E-Mail support@crowdstrike.com for help on enabling the Phantom integration
on your instance.

##### Testing connectivity

After creating the Falcon Sandbox asset, we recommended to test the application server connectivity.
That way, you make sure that the provided base URL and API credentials are working correctly.


### Configuration Variables
The below configuration variables are required for this Connector to operate.  These variables are specified when configuring a Falcon Sandbox asset in SOAR.

VARIABLE | REQUIRED | TYPE | DESCRIPTION
-------- | -------- | ---- | -----------
**base\_url** |  required  | string | Base URL to Falcon Sandbox Application Server
**verify\_server\_cert** |  required  | boolean | Verify server certificate
**api\_key** |  required  | password | API Key

### Supported Actions  
[search terms](#action-search-terms) - Search for samples in Falcon Sandbox database using search terms  
[hunt similar](#action-hunt-similar) - Search for similar samples by given Sha256 hash in the Falcon Sandbox database  
[hunt ip](#action-hunt-ip) - Search for a given IP in the Falcon Sandbox database  
[hunt hash](#action-hunt-hash) - Search for a file by one kind of hash\(Sha1, Md5, Sha256\) in the Falcon Sandbox database  
[hunt file](#action-hunt-file) - Search for a file by one kind of data\(Sha1, Md5, Sha256 or File name\) in the Falcon Sandbox database  
[hunt malware family](#action-hunt-malware-family) - Search for a given malware family in the Falcon Sandbox database  
[hunt domain](#action-hunt-domain) - Search for a given domain in the Falcon Sandbox database  
[hunt url](#action-hunt-url) - Search for a given URL in the Falcon Sandbox database  
[get file from url](#action-get-file-from-url) - Download file from a url  
[get pcap](#action-get-pcap) - Download the pcap file of sample from Falcon Sandbox and add it to vault  
[get file](#action-get-file) - Download sample result data from Falcon Sandbox and add it to vault  
[get report](#action-get-report) - Fetch results of an already completed analysis in the Falcon Sandbox  
[check status](#action-check-status) - Check status of sample \(file or URL\) submitted in the Falcon Sandbox  
[check url hash](#action-check-url-hash) - Determine a SHA256 that an online file or URL submission will have when being processed by the Falcon Sandbox  
[detonate url](#action-detonate-url) - Detonate a URL in the Falcon Sandbox  
[detonate online file](#action-detonate-online-file) - Detonate an online file in the Falcon Sandbox  
[detonate file](#action-detonate-file) - Detonate the file in the Falcon Sandbox  
[test connectivity](#action-test-connectivity) - Validate the asset configuration for connectivity  

## action: 'search terms'
Search for samples in Falcon Sandbox database using search terms

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**file\_name** |  optional  | File name e\.g\. invoice\.exe | string |  `file name` 
**file\_type** |  optional  | File type e\.g\. docx | string | 
**file\_type\_substring** |  optional  | File type description e\.g\. PE32 executable | string | 
**environment\_id** |  optional  | Environment Id | numeric | 
**country** |  optional  | Country \(3 digit ISO\) e\.g\. swe | string | 
**verdict** |  optional  | Verdict | string |  `falcon sandbox verdict` 
**av\_detection** |  optional  | AV Multiscan range e\.g\. 50\-70 \(min 0, max 100\) | string | 
**av\_family\_substring** |  optional  | AV Family Substring e\.g\. nemucod | string |  `malware family` 
**hashtag** |  optional  | Hashtag e\.g\. ransomware | string |  `falcon sandbox tag` 
**port** |  optional  | Port e\.g\. 8080 | numeric |  `port` 
**host** |  optional  | Host e\.g\. 192\.168\.0\.1 | string |  `ip` 
**domain** |  optional  | Domain e\.g\. checkip\.dyndns\.org | string |  `domain` 
**url** |  optional  | HTTP Request Substring e\.g\. google | string |  `url` 
**similar\_samples** |  optional  | Similar Samples e\.g\. <sha256> | string |  `sha256` 
**similar\_context** |  optional  | Sample Context e\.g\. <sha256> | string |  `sha256` 
**imphash** |  optional  |  | string |  `imphash` 
**ssdeep** |  optional  |  | string |  `ssdeep` 
**authentihash** |  optional  |  | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.message | string | 
action\_result\.data\.\*\.submit\_name | string |  `file name` 
action\_result\.data\.\*\.job\_id | string |  `falcon sandbox job id` 
action\_result\.data\.\*\.sha256 | string |  `sha256` 
action\_result\.data\.\*\.environment | string | 
action\_result\.data\.\*\.type | string | 
action\_result\.data\.\*\.environment\_id | numeric | 
action\_result\.data\.\*\.environment\_description | string | 
action\_result\.data\.\*\.verdict | string |  `falcon sandbox verdict` 
action\_result\.data\.\*\.threat\_score | string | 
action\_result\.data\.\*\.threat\_score\_verbose | string | 
action\_result\.summary\.found | numeric | 
action\_result\.summary\.found\_by\_verdict\_name\.unknown | numeric | 
action\_result\.summary\.found\_by\_verdict\_name\.no\_verdict | numeric | 
action\_result\.summary\.found\_by\_verdict\_name\.no\_specific\_threat | numeric | 
action\_result\.summary\.found\_by\_verdict\_name\.whitelisted | numeric | 
action\_result\.summary\.found\_by\_verdict\_name\.suspicious | numeric | 
action\_result\.summary\.found\_by\_verdict\_name\.malicious | numeric | 
action\_result\.parameter\.similar\_context | numeric |  `sha256` 
action\_result\.parameter\.port | numeric |  `port` 
action\_result\.parameter\.host | string |  `ip` 
action\_result\.parameter\.ssdeep | string |  `ssdeep` 
action\_result\.parameter\.av\_family\_substring | string |  `malware family` 
action\_result\.parameter\.file\_type | string | 
action\_result\.parameter\.hashtag | string |  `falcon sandbox tag` 
action\_result\.parameter\.file\_type\_substring | string | 
action\_result\.parameter\.imphash | string |  `imphash` 
action\_result\.parameter\.av\_detection | string | 
action\_result\.parameter\.authentihash | string | 
action\_result\.parameter\.country | string | 
action\_result\.parameter\.similar\_samples | string |  `sha256` 
action\_result\.parameter\.environment\_id | numeric | 
action\_result\.parameter\.domain | string |  `domain` 
action\_result\.parameter\.verdict | string |  `falcon sandbox verdict` 
action\_result\.parameter\.file\_name | string |  `file name` 
action\_result\.parameter\.url | string |  `url` 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'hunt similar'
Search for similar samples by given Sha256 hash in the Falcon Sandbox database

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**sha256** |  required  | Sample Sha256 | string |  `sha256` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.message | string | 
action\_result\.data\.\*\.submit\_name | string |  `file name` 
action\_result\.data\.\*\.job\_id | string |  `falcon sandbox job id` 
action\_result\.data\.\*\.sha256 | string |  `sha256` 
action\_result\.data\.\*\.environment | string | 
action\_result\.data\.\*\.type | string | 
action\_result\.data\.\*\.environment\_id | numeric | 
action\_result\.data\.\*\.environment\_description | string | 
action\_result\.data\.\*\.verdict | string |  `falcon sandbox verdict` 
action\_result\.data\.\*\.threat\_score | string | 
action\_result\.data\.\*\.threat\_score\_verbose | string | 
action\_result\.summary\.found | numeric | 
action\_result\.summary\.found\_by\_verdict\_name\.unknown | numeric | 
action\_result\.summary\.found\_by\_verdict\_name\.no\_verdict | numeric | 
action\_result\.summary\.found\_by\_verdict\_name\.no\_specific\_threat | numeric | 
action\_result\.summary\.found\_by\_verdict\_name\.whitelisted | numeric | 
action\_result\.summary\.found\_by\_verdict\_name\.suspicious | numeric | 
action\_result\.summary\.found\_by\_verdict\_name\.malicious | numeric | 
action\_result\.parameter\.sha256 | string |  `sha256` 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'hunt ip'
Search for a given IP in the Falcon Sandbox database

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**host** |  required  | IP | string |  `ip` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.message | string | 
action\_result\.data\.\*\.submit\_name | string |  `file name` 
action\_result\.data\.\*\.job\_id | string |  `falcon sandbox job id` 
action\_result\.data\.\*\.sha256 | string |  `sha256` 
action\_result\.data\.\*\.environment | string | 
action\_result\.data\.\*\.type | string | 
action\_result\.data\.\*\.environment\_id | numeric | 
action\_result\.data\.\*\.environment\_description | string | 
action\_result\.data\.\*\.verdict | string |  `falcon sandbox verdict` 
action\_result\.data\.\*\.threat\_score | string | 
action\_result\.data\.\*\.threat\_score\_verbose | string | 
action\_result\.summary\.found | numeric | 
action\_result\.summary\.found\_by\_verdict\_name\.unknown | numeric | 
action\_result\.summary\.found\_by\_verdict\_name\.no\_verdict | numeric | 
action\_result\.summary\.found\_by\_verdict\_name\.no\_specific\_threat | numeric | 
action\_result\.summary\.found\_by\_verdict\_name\.whitelisted | numeric | 
action\_result\.summary\.found\_by\_verdict\_name\.suspicious | numeric | 
action\_result\.summary\.found\_by\_verdict\_name\.malicious | numeric | 
action\_result\.parameter\.host | string |  `ip` 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'hunt hash'
Search for a file by one kind of hash\(Sha1, Md5, Sha256\) in the Falcon Sandbox database

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**hash** |  required  | Sha1, Md5, Sha256 | string |  `sha256`  `sha1`  `md5` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.message | string | 
action\_result\.data\.\*\.submit\_name | string |  `file name` 
action\_result\.data\.\*\.job\_id | string |  `falcon sandbox job id` 
action\_result\.data\.\*\.sha256 | string |  `sha256` 
action\_result\.data\.\*\.environment | string | 
action\_result\.data\.\*\.type | string | 
action\_result\.data\.\*\.environment\_id | numeric | 
action\_result\.data\.\*\.environment\_description | string | 
action\_result\.data\.\*\.verdict | string |  `falcon sandbox verdict` 
action\_result\.data\.\*\.threat\_score | string | 
action\_result\.data\.\*\.threat\_score\_verbose | string | 
action\_result\.summary\.found | numeric | 
action\_result\.summary\.found\_by\_verdict\_name\.unknown | numeric | 
action\_result\.summary\.found\_by\_verdict\_name\.no\_verdict | numeric | 
action\_result\.summary\.found\_by\_verdict\_name\.no\_specific\_threat | numeric | 
action\_result\.summary\.found\_by\_verdict\_name\.whitelisted | numeric | 
action\_result\.summary\.found\_by\_verdict\_name\.suspicious | numeric | 
action\_result\.summary\.found\_by\_verdict\_name\.malicious | numeric | 
action\_result\.parameter\.hash | string |  `sha256`  `sha1`  `md5` 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'hunt file'
Search for a file by one kind of data\(Sha1, Md5, Sha256 or File name\) in the Falcon Sandbox database

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**file\_name** |  required  | File name | string |  `file name` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.message | string | 
action\_result\.data\.\*\.submit\_name | string |  `file name` 
action\_result\.data\.\*\.job\_id | string |  `falcon sandbox job id` 
action\_result\.data\.\*\.sha256 | string |  `sha256` 
action\_result\.data\.\*\.environment | string | 
action\_result\.data\.\*\.type | string | 
action\_result\.data\.\*\.environment\_id | numeric | 
action\_result\.data\.\*\.environment\_description | string | 
action\_result\.data\.\*\.verdict | string |  `falcon sandbox verdict` 
action\_result\.data\.\*\.threat\_score | string | 
action\_result\.data\.\*\.threat\_score\_verbose | string | 
action\_result\.summary\.found | numeric | 
action\_result\.summary\.found\_by\_verdict\_name\.unknown | numeric | 
action\_result\.summary\.found\_by\_verdict\_name\.no\_verdict | numeric | 
action\_result\.summary\.found\_by\_verdict\_name\.no\_specific\_threat | numeric | 
action\_result\.summary\.found\_by\_verdict\_name\.whitelisted | numeric | 
action\_result\.summary\.found\_by\_verdict\_name\.suspicious | numeric | 
action\_result\.summary\.found\_by\_verdict\_name\.malicious | numeric | 
action\_result\.parameter\.file\_name | string |  `file name` 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'hunt malware family'
Search for a given malware family in the Falcon Sandbox database

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**malware\_family** |  required  | AV Family Substring e\.g\. nemucod | string |  `malware family` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.message | string | 
action\_result\.data\.\*\.submit\_name | string |  `file name` 
action\_result\.data\.\*\.job\_id | string |  `falcon sandbox job id` 
action\_result\.data\.\*\.sha256 | string |  `sha256` 
action\_result\.data\.\*\.environment | string | 
action\_result\.data\.\*\.type | string | 
action\_result\.data\.\*\.environment\_id | numeric | 
action\_result\.data\.\*\.environment\_description | string | 
action\_result\.data\.\*\.verdict | string |  `falcon sandbox verdict` 
action\_result\.data\.\*\.threat\_score | string | 
action\_result\.data\.\*\.threat\_score\_verbose | string | 
action\_result\.summary\.found | numeric | 
action\_result\.summary\.found\_by\_verdict\_name\.unknown | numeric | 
action\_result\.summary\.found\_by\_verdict\_name\.no\_verdict | numeric | 
action\_result\.summary\.found\_by\_verdict\_name\.no\_specific\_threat | numeric | 
action\_result\.summary\.found\_by\_verdict\_name\.whitelisted | numeric | 
action\_result\.summary\.found\_by\_verdict\_name\.suspicious | numeric | 
action\_result\.summary\.found\_by\_verdict\_name\.malicious | numeric | 
action\_result\.parameter\.malware\_family | string |  `malware family` 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'hunt domain'
Search for a given domain in the Falcon Sandbox database

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**domain** |  required  | Domain e\.g\. checkip\.dyndns\.org | string |  `domain` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.message | string | 
action\_result\.data\.\*\.submit\_name | string |  `file name` 
action\_result\.data\.\*\.job\_id | string |  `falcon sandbox job id` 
action\_result\.data\.\*\.sha256 | string |  `sha256` 
action\_result\.data\.\*\.environment | string | 
action\_result\.data\.\*\.type | string | 
action\_result\.data\.\*\.environment\_id | numeric | 
action\_result\.data\.\*\.environment\_description | string | 
action\_result\.data\.\*\.verdict | string |  `falcon sandbox verdict` 
action\_result\.data\.\*\.threat\_score | string | 
action\_result\.data\.\*\.threat\_score\_verbose | string | 
action\_result\.summary\.found | numeric | 
action\_result\.summary\.found\_by\_verdict\_name\.unknown | numeric | 
action\_result\.summary\.found\_by\_verdict\_name\.no\_verdict | numeric | 
action\_result\.summary\.found\_by\_verdict\_name\.no\_specific\_threat | numeric | 
action\_result\.summary\.found\_by\_verdict\_name\.whitelisted | numeric | 
action\_result\.summary\.found\_by\_verdict\_name\.suspicious | numeric | 
action\_result\.summary\.found\_by\_verdict\_name\.malicious | numeric | 
action\_result\.parameter\.domain | string |  `domain` 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'hunt url'
Search for a given URL in the Falcon Sandbox database

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**url** |  required  | HTTP Request Substring e\.g\. google | string |  `url` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.message | string | 
action\_result\.data\.\*\.submit\_name | string |  `file name` 
action\_result\.data\.\*\.job\_id | string |  `falcon sandbox job id` 
action\_result\.data\.\*\.sha256 | string |  `sha256` 
action\_result\.data\.\*\.environment | string | 
action\_result\.data\.\*\.type | string | 
action\_result\.data\.\*\.environment\_id | numeric | 
action\_result\.data\.\*\.environment\_description | string | 
action\_result\.data\.\*\.verdict | string |  `falcon sandbox verdict` 
action\_result\.data\.\*\.threat\_score | string | 
action\_result\.data\.\*\.threat\_score\_verbose | string | 
action\_result\.summary\.found | numeric | 
action\_result\.summary\.found\_by\_verdict\_name\.unknown | numeric | 
action\_result\.summary\.found\_by\_verdict\_name\.no\_verdict | numeric | 
action\_result\.summary\.found\_by\_verdict\_name\.no\_specific\_threat | numeric | 
action\_result\.summary\.found\_by\_verdict\_name\.whitelisted | numeric | 
action\_result\.summary\.found\_by\_verdict\_name\.suspicious | numeric | 
action\_result\.summary\.found\_by\_verdict\_name\.malicious | numeric | 
action\_result\.parameter\.url | string |  `url` 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'get file from url'
Download file from a url

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**url** |  required  | Url containing file | string |  `url` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.message | string | 
action\_result\.data\.\*\.file\_name | string |  `file name` 
action\_result\.data\.\*\.vault\_id | string |  `vault id` 
action\_result\.data\.\*\.file\_type | string | 
action\_result\.parameter\.url | string |  `url` 
action\_result\.summary\.file\_name | string |  `file name` 
action\_result\.summary\.vault\_id | string |  `vault id` 
action\_result\.summary\.file\_type | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'get pcap'
Download the pcap file of sample from Falcon Sandbox and add it to vault

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**id** |  required  | Sample Id in one of format\: 'jobId' or 'sha256\:environmentId' | string |  `falcon sandbox job id` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.message | string | 
action\_result\.data\.\*\.file\_name | string |  `file name` 
action\_result\.data\.\*\.vault\_id | string |  `vault id` 
action\_result\.data\.\*\.file\_type | string | 
action\_result\.parameter\.id | string |  `falcon sandbox job id` 
action\_result\.summary\.file\_name | string |  `file name` 
action\_result\.summary\.vault\_id | string |  `vault id` 
action\_result\.summary\.file\_type | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'get file'
Download sample result data from Falcon Sandbox and add it to vault

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**id** |  required  | Sample Id in one of format\: 'jobId' or 'sha256\:environmentId' | string |  `falcon sandbox job id` 
**file\_type** |  required  | File type | string | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.message | string | 
action\_result\.data\.\*\.file\_name | string |  `file name` 
action\_result\.data\.\*\.vault\_id | string |  `vault id` 
action\_result\.data\.\*\.file\_type | string | 
action\_result\.parameter\.file\_type | string | 
action\_result\.parameter\.id | string |  `falcon sandbox job id` 
action\_result\.summary\.file\_name | string |  `file name` 
action\_result\.summary\.vault\_id | string |  `vault id` 
action\_result\.summary\.file\_type | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'get report'
Fetch results of an already completed analysis in the Falcon Sandbox

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**id** |  required  | Sample Id in one of format\: 'jobId' or 'sha256\:environmentId' | string |  `falcon sandbox job id` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.message | string | 
action\_result\.data\.job\_id | string |  `falcon sandbox job id` 
action\_result\.data\.\*\.environment\_id | numeric | 
action\_result\.data\.\*\.submit\_name | string |  `file name` 
action\_result\.data\.\*\.target\_url | string |  `url` 
action\_result\.data\.\*\.size | string |  `file size` 
action\_result\.data\.\*\.type | string | 
action\_result\.data\.\*\.sha256 | string |  `sha256` 
action\_result\.data\.\*\.md5 | string |  `md5` 
action\_result\.data\.\*\.sha1 | string |  `sha1` 
action\_result\.data\.\*\.ssdeep | string |  `ssdeep` 
action\_result\.data\.\*\.imphash | string |  `imphash` 
action\_result\.data\.\*\.classification\_tags\.\* | string |  `malware family`  `falcon sandbox tag` 
action\_result\.data\.\*\.url\_analysis | boolean | 
action\_result\.data\.\*\.threat\_score | numeric | 
action\_result\.data\.\*\.interesting | boolean | 
action\_result\.data\.\*\.verdict | string |  `falcon sandbox verdict` 
action\_result\.data\.\*\.domains\.\* | string |  `domain` 
action\_result\.data\.\*\.hosts\.\* | string |  `ip` 
action\_result\.data\.\*\.compromised\_hosts\.\* | string |  `ip` 
action\_result\.data\.\*\.total\_network\_connections | numeric | 
action\_result\.data\.\*\.total\_processes | numeric | 
action\_result\.data\.\*\.total\_signatures | numeric | 
action\_result\.parameter\.id | string |  `falcon sandbox job id` 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'check status'
Check status of sample \(file or URL\) submitted in the Falcon Sandbox

Type: **investigate**  
Read only: **True**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**id** |  required  | Sample Id in one of format\: 'jobId' or 'sha256\:environmentId' | string |  `falcon sandbox job id` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.message | string | 
action\_result\.parameter\.id | string |  `falcon sandbox job id` 
action\_result\.data\.\*\.status | string | 
action\_result\.data\.\*\.error\_msg | string | 
action\_result\.summary\.status | string | 
action\_result\.summary\.error\_msg | string | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'check url hash'
Determine a SHA256 that an online file or URL submission will have when being processed by the Falcon Sandbox

Type: **investigate**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**url** |  required  | Url to check | string |  `url` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.message | string | 
action\_result\.parameter\.url | string |  `url` 
action\_result\.data\.\*\.sha256 | string |  `sha256` 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'detonate url'
Detonate a URL in the Falcon Sandbox

Type: **investigate**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**url** |  required  | Url | string |  `url` 
**environment\_id** |  required  | Environment Id | numeric | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.message | string | 
action\_result\.parameter\.environment\_id | numeric | 
action\_result\.parameter\.url | string |  `url` 
action\_result\.data\.job\_id | string |  `falcon sandbox job id` 
action\_result\.data\.\*\.environment\_id | numeric | 
action\_result\.data\.\*\.submit\_name | string |  `file name` 
action\_result\.data\.\*\.target\_url | string |  `url` 
action\_result\.data\.\*\.size | string |  `file size` 
action\_result\.data\.\*\.type | string | 
action\_result\.data\.\*\.sha256 | string |  `sha256` 
action\_result\.data\.\*\.md5 | string |  `md5` 
action\_result\.data\.\*\.sha1 | string |  `sha1` 
action\_result\.data\.\*\.ssdeep | string |  `ssdeep` 
action\_result\.data\.\*\.imphash | string |  `imphash` 
action\_result\.data\.\*\.classification\_tags\.\* | string |  `malware family`  `falcon sandbox tag` 
action\_result\.data\.\*\.url\_analysis | boolean | 
action\_result\.data\.\*\.threat\_score | numeric | 
action\_result\.data\.\*\.interesting | boolean | 
action\_result\.data\.\*\.verdict | string |  `falcon sandbox verdict` 
action\_result\.data\.\*\.domains\.\* | string |  `domain` 
action\_result\.data\.\*\.hosts\.\* | string |  `ip` 
action\_result\.data\.\*\.compromised\_hosts\.\* | string |  `ip` 
action\_result\.data\.\*\.total\_network\_connections | numeric | 
action\_result\.data\.\*\.total\_processes | numeric | 
action\_result\.data\.\*\.total\_signatures | numeric | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'detonate online file'
Detonate an online file in the Falcon Sandbox

Type: **investigate**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**url** |  required  | Url | string |  `url` 
**environment\_id** |  required  | Environment Id | numeric | 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.message | string | 
action\_result\.parameter\.environment\_id | numeric | 
action\_result\.parameter\.url | string |  `url` 
action\_result\.data\.job\_id | string |  `falcon sandbox job id` 
action\_result\.data\.\*\.environment\_id | numeric | 
action\_result\.data\.\*\.submit\_name | string |  `file name` 
action\_result\.data\.\*\.target\_url | string |  `url` 
action\_result\.data\.\*\.size | string |  `file size` 
action\_result\.data\.\*\.type | string | 
action\_result\.data\.\*\.sha256 | string |  `sha256` 
action\_result\.data\.\*\.md5 | string |  `md5` 
action\_result\.data\.\*\.sha1 | string |  `sha1` 
action\_result\.data\.\*\.ssdeep | string |  `ssdeep` 
action\_result\.data\.\*\.imphash | string |  `imphash` 
action\_result\.data\.\*\.classification\_tags\.\* | string |  `malware family`  `falcon sandbox tag` 
action\_result\.data\.\*\.url\_analysis | boolean | 
action\_result\.data\.\*\.threat\_score | numeric | 
action\_result\.data\.\*\.interesting | boolean | 
action\_result\.data\.\*\.verdict | string |  `falcon sandbox verdict` 
action\_result\.data\.\*\.domains\.\* | string |  `domain` 
action\_result\.data\.\*\.hosts\.\* | string |  `ip` 
action\_result\.data\.\*\.compromised\_hosts\.\* | string |  `ip` 
action\_result\.data\.\*\.total\_network\_connections | numeric | 
action\_result\.data\.\*\.total\_processes | numeric | 
action\_result\.data\.\*\.total\_signatures | numeric | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'detonate file'
Detonate the file in the Falcon Sandbox

Type: **investigate**  
Read only: **False**

#### Action Parameters
PARAMETER | REQUIRED | DESCRIPTION | TYPE | CONTAINS
--------- | -------- | ----------- | ---- | --------
**vault\_id** |  required  | Vault ID of file to submit | string |  `vault id` 
**environment\_id** |  required  | Environment ID | numeric | 
**file\_name** |  required  | File name to use | string |  `file name` 

#### Action Output
DATA PATH | TYPE | CONTAINS
--------- | ---- | --------
action\_result\.status | string | 
action\_result\.message | string | 
action\_result\.parameter\.vault\_id | string |  `vault id` 
action\_result\.parameter\.environment\_id | numeric | 
action\_result\.parameter\.file\_name | string |  `file name` 
action\_result\.data\.job\_id | string |  `falcon sandbox job id` 
action\_result\.data\.\*\.environment\_id | numeric | 
action\_result\.data\.\*\.submit\_name | string |  `file name` 
action\_result\.data\.\*\.target\_url | string |  `url` 
action\_result\.data\.\*\.size | string |  `file size` 
action\_result\.data\.\*\.type | string | 
action\_result\.data\.\*\.sha256 | string |  `sha256` 
action\_result\.data\.\*\.md5 | string |  `md5` 
action\_result\.data\.\*\.sha1 | string |  `sha1` 
action\_result\.data\.\*\.ssdeep | string |  `ssdeep` 
action\_result\.data\.\*\.imphash | string |  `imphash` 
action\_result\.data\.\*\.classification\_tags\.\* | string |  `malware family`  `falcon sandbox tag` 
action\_result\.data\.\*\.url\_analysis | boolean | 
action\_result\.data\.\*\.threat\_score | numeric | 
action\_result\.data\.\*\.interesting | boolean | 
action\_result\.data\.\*\.verdict | string |  `falcon sandbox verdict` 
action\_result\.data\.\*\.domains\.\* | string |  `domain` 
action\_result\.data\.\*\.hosts\.\* | string |  `ip` 
action\_result\.data\.\*\.compromised\_hosts\.\* | string |  `ip` 
action\_result\.data\.\*\.total\_network\_connections | numeric | 
action\_result\.data\.\*\.total\_processes | numeric | 
action\_result\.data\.\*\.total\_signatures | numeric | 
summary\.total\_objects | numeric | 
summary\.total\_objects\_successful | numeric |   

## action: 'test connectivity'
Validate the asset configuration for connectivity

Type: **test**  
Read only: **True**

#### Action Parameters
No parameters are required for this action

#### Action Output
No Output