create table posts
(
    id                    integer not null primary key,
    posttypeid            varchar(2),
    acceptedanswerid      integer,
    parentid              integer,
    creationdate          timestamp,
    deletiondate          timestamp,
    score                 integer,
    viewcount             integer,
    body                  text,
    owneruserid           integer,
    ownerdisplayname      varchar(40),
    lasteditoruserid      integer,
    lasteditordisplayname varchar(40),
    lasteditdate          timestamp,
    lastactivitydate      timestamp,
    title                 varchar(250),
    tags                  varchar(250),
    answercount           integer,
    commentcount          integer,
    favoritecount         integer,
    closeddate            timestamp,
    communityowneddate    timestamp,
    contentlicense        varchar(12),
    creationyear          varchar(5)
);

create index idx_posts_creationdate_01 on posts (creationdate);
create index idx_posts_01 on posts (owneruserid);

create table postsbody
(
    id   integer not null primary key,
    body text
);

create table tags
(
    id              integer not null primary key,
    tagname         varchar(35),
    count           integer,
    excerptpostid   integer,
    wikipostid      integer,
    ismoderatoronly varchar(2),
    isrequired      varchar(2)
);

create table users
(
    id              integer not null primary key,
    reputation      integer,
    creationdate    timestamp,
    displayname     varchar(40),
    lastaccessdate  timestamp,
    websiteurl      varchar(200),
    location        varchar(100),
    aboutme         text,
    views           integer,
    upvotes         integer,
    downvotes       integer,
    profileimageurl varchar(200),
    emailhash       varchar(32),
    accountid       integer,
    creationyear    varchar(5)
);

create table votes
(
    id           integer not null primary key,
    postid       integer,
    votetypeid   varchar(2),
    userid       integer,
    creationdate timestamp,
    bountyamount integer
);

create index idx_votes_01 on votes (postid, votetypeid);

create table badges
(
    id       integer not null primary key,
    userid   integer,
    name     varchar(40),
    date     timestamp,
    class    varchar(2),
    tagbased bit
);

create table comments
(
    id              integer not null primary key,
    postid          integer,
    score           integer,
    text            text,
    creationdate    timestamp,
    userdisplayname varchar(40),
    userid          integer,
    contentlicense  varchar(12)
);
