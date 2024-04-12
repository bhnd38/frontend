SELECT name
from songs
WHERE name
LIKE '%feat%';

--WHERE 조건에 패턴을 필터링하는 방법
--SELECT 컬럼명, ... FROM 테이블명 WHERE 컬럼 LIKE 패턴;
--A로 시작하는 문자열 패턴: 'A%'
--A가 두번 나오는 문자열 패턴: '%A%A%'
--A로 시작해 B로 끝나는 문자열 패턴: 'A%B'
--A와 B사이에 문자 한개가 있는 문자열 패턴: 'A_B'
--ABC 문자열이 포함된 패턴: '%ABC%'
--특수문자(ex. $)를 패턴에 넣는 방법: escape '$';


--주의
--LIKE 절에서는 대문자와 소문자를 구별하지 않는다.
