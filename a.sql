SELECT count(*) AS count_1
FROM (SELECT cert_operation_record.id AS id,
             employee_1.id            AS `employee.id`,
             jobinfomation_1.id       AS `job_info.id`,
             department_history_1.id  AS `position.id`,
             department_history_2.id  AS `department.id`,
             department_history_3.id  AS `unit.id`
      FROM cert_operation_record
               INNER JOIN employee AS employee_1
                          ON employee_1.id = cert_operation_record.employee_id AND employee_1.company_id = 768
               INNER JOIN jobinfomation AS jobinfomation_1
                          ON jobinfomation_1.employee_id = cert_operation_record.employee_id AND
                             jobinfomation_1.begin_date <= '2023-02-01' AND jobinfomation_1.end_date > '2023-02-01' AND
                             jobinfomation_1.position_type = 1 AND jobinfomation_1.company_id = 768
               LEFT OUTER JOIN department_history AS department_history_1
                               ON jobinfomation_1.position_id = department_history_1.origin_id AND
                                  department_history_1.begin_date <= '2023-02-01' AND
                                  department_history_1.end_date > '2023-02-01' AND department_history_1.company_id = 768
               LEFT OUTER JOIN department_history AS department_history_2
                               ON department_history_1.parent_id = department_history_2.origin_id AND
                                  department_history_2.begin_date <= '2023-02-01' AND
                                  department_history_2.end_date > '2023-02-01' AND department_history_2.company_id = 768
               LEFT OUTER JOIN department_history AS department_history_3
                               ON department_history_2.subordinate_unit_id = department_history_3.origin_id AND
                                  department_history_3.begin_date <= '2023-02-01' AND
                                  department_history_3.end_date > '2023-02-01' AND department_history_3.company_id = 768
               INNER JOIN (SELECT department_hierarchy.department_id AS id
                           FROM department_hierarchy
                           WHERE department_hierarchy.l1_id = 19
                             AND department_hierarchy.company_id = 768
                             AND department_hierarchy.begin_date <= '2023-02-01 00:00:00'
                             AND department_hierarchy.end_date > '2023-02-01 00:00:00'
                             AND department_hierarchy.enabled IN (1, 0)) AS anon_2
                          ON anon_2.id = department_history_2.origin_id
      WHERE cert_operation_record.company_id = 768
        AND cert_operation_record.operate_time >= '2023-02-01'
        AND cert_operation_record.operate_time <= '2023-02-02') AS anon_1