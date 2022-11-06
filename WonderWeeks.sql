create database wonder_weeks;
use wonder_weeks;
create table wonderweeks(
week_id int primary key auto_increment,
mental_leap char(50),
aproximate_age int,
development_info longtext
);
select * from wonderweeks;
insert into wonderweeks(mental_leap,aproximate_age, development_info) values
('Leap 1', 5, 'Changing Sensations. Baby starts becoming more aware of physical stimuli.'),
('Leap 2', 8, 'Patterns. Baby recognizes patterns an notices he is separate from the world.Increase use in senses'),
('Leap 3', 12, 'Smooth transitions. Baby literally starts beingg less jerky. Starts getting more control over his body'),
('Leap 4', 19, 'Events. Baby recognize a sequence of events.(Pick up toy, put in mounth, etc.'),
('Leap 5', 26, 'Relationships. Baby starts to notice physical distances and the initial basics of cause and effect.'),
('Leap 6', 37, 'Categories. Baby learns that items can be put into groups'),
('Leap 7', 46, 'Sequences. Baby learns there is an order to things and can start to replicate this order'),
('Leap 8', 55, 'Programs.Baby learns there is more than one way to reach the same end'),
('Leap 9', 64, 'Principles.Baby can start planning how to accomplish basic goals.'),
('Leap 10', 75, 'Systems. Baby starts understanding different systems of how the world is set up.');
